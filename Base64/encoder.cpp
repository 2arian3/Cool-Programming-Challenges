#include <iostream>
#include <fstream>
#include <string>

char base64_mapping(char binary){
    char result = binary < 26 ? binary + 'A' :
                  binary < 52 ? binary + 'a' - 26 :
                  binary < 62 ? binary + '0' - 52 :
                  binary == 62 ? '+' : '/';
    return result;
}

std::string base64_encoding(unsigned char* text){
    std::string converted;
    converted += base64_mapping(text[0] >> 2);
    converted += base64_mapping((text[1] >> 4) | ((text[0] & 0b11) << 4));
    converted += base64_mapping((text[2] >> 6) | ((text[1] & 0b1111) << 2));
    converted += base64_mapping(text[2] & 0b111111);
    return converted;
}

int main(int argc, char **argv) {
    if (argc != 2){
        std::cout << "Illegal input..." << std::endl;
        return -1;
    }

    std::string encoded;
    std::ifstream input_file (argv[1], std::ios::ate | std::ios::binary);
    if (input_file.is_open()){

        std::streampos size = input_file.tellg();
        char *buffer = new char[size];
        unsigned char *temp = new unsigned char[3];
        input_file.seekg(0, std::ios::beg);
        input_file.read(buffer, size);

        int j = 0;
        for (int i = 0; i < size; i++){
            temp[j++] = buffer[i] & 0xFF;
            if (j == 3){
                j = 0;
                encoded += base64_encoding(temp);
                temp = new unsigned char[3];
            }
        }

        if (int(size)%3) {
            for (int i = 0; i < 3 - int(size)%3; i++)
                temp[3-i] = 0;
            encoded += base64_encoding(temp);
            for (int i = 0; i < 3 - int(size)%3; i++)
                encoded += '=';
        }

        delete[] buffer;
        std::ofstream output_file ("encoded_input");
        output_file << encoded;
        input_file.close();
        output_file.close();
    } else{
        std::cout << "Cannot open the given file :/" << std::endl;
        return -1;
    }
    return 0;
}