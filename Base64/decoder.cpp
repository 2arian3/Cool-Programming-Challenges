#include <iostream>
#include <fstream>
#include <string>

int base64_mapping(char character){
    int result = character >= 'A' && character <= 'Z' ?  int(character) - int('A'):
                 character >= 'a' && character <= 'z' ? int(character) - int('a') + 26:
                 character >= '0' && character <= '9' ? int(character) - int('0') + 52:
                 character == '+' ? 62 : 63;
    return result;
}

std::string base64_decoding(std::string text){
    std::string converted;
    converted += char ((base64_mapping(text[0]) << 2) | (base64_mapping(text[1]) >> 4));
    converted += char (((base64_mapping(text[1]) & 0b1111) << 4) | ((base64_mapping(text[2]) & 0b111100) >> 2));
    converted += char (((base64_mapping(text[2]) & 0b11) << 6) | (base64_mapping(text[3])));
    return converted;
}

int main(int argc, char **argv) {
    if(argc != 2){
        std::cout << "Illegal input..." << std::endl;
        return -1;
    }

    std::string read, decoded;
    std::ifstream input_file (argv[1], std::ios::ate | std::ios::binary);
    if(input_file.is_open()) {

        std::streampos size = input_file.tellg();
        char *buffer = new char[size];
        input_file.seekg(0, std::ios::beg);
        input_file.read(buffer, size);

        for (int i = 0; i < size; i++) {
            read += buffer[i];
            if (read.size() == 4) {
                decoded += base64_decoding(read);
                read = "";
            }
        }

        int padding = std::count(buffer, buffer + size, '=');
        while (padding) {
            padding--;
            decoded.pop_back();
        }

        delete[] buffer;
        std::ofstream output_file("decoded_input", std::ios::out | std::ios::binary);
        output_file << decoded;
        input_file.close();
        output_file.close();
    } else{
        std::cout << "Cannot open the given file :/" << std::endl;
        return -1;
    }
    return 0;
}