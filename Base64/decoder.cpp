#include <iostream>
#include <fstream>

int base64_mapping(char character){
    int result = character >= 'A' && character <= 'Z' ?  int(character) - int('A'):
                 character >= 'a' && character <= 'z' ? int(character) - int('a') + 26:
                 character >= '0' && character <= '9' ? int(character) - int('0') + 52:
                 character == '+' ? 62 : 63;
    return result;
}

std::string base64_decoding(std::string text){
    std::string converted;
    converted += char ((base64_mapping(text[0]) << 0b10) | (base64_mapping(text[1]) >> 0b100));
    converted += char (((base64_mapping(text[1]) & 0b1111) << 0b100) | ((base64_mapping(text[2]) & 0b111100) >> 0b10));
    converted += char (((base64_mapping(text[2]) & 0b11) << 0b110) | (base64_mapping(text[3])));
    return converted;
}

int main(int argc, char **argv) {
    if(argc != 2){
        std::cout << "Illegal input..." << std::endl;
        return -1;
    } else{
        std::string directory = argv[1];
        if(directory.size() < 4 ||  directory.substr(directory.size()-4, 4) != ".txt"){
            std::cout << "Wrong directory. must be text file :)" << std::endl;
            return -1;
        }
    }
    std::string temp, read, decoded;
    std::ifstream text (argv[1]);
    if(text.is_open()){
        while(!text.eof()){
            getline(text, temp);
            for(int i = 0; i < temp.size(); i++){
                read += temp[i];
                if(read.size() == 4){
                    decoded += base64_decoding(read);
                    read = "";
                }
            }
            int padding = std::count(temp.begin(), temp.end(), '=');
            while (padding){
                padding --;
                decoded.pop_back();
            }
        }
        std::ofstream output ("decoded.txt");
        output << decoded;
        text.close();
        output.close();
    } else{
        std::cout << "Cannot open the text file :/" << std::endl;
        return -1;
    }
    return 0;
}