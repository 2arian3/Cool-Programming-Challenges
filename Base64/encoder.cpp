#include <iostream>
#include <fstream>

char base64_mapping(int binary){
    char result = binary < 26 ? binary + 'A' :
                  binary < 52 ? binary + 'a' - 26 :
                  binary < 62 ? binary + '0' - 52 :
                  binary == 62 ? '+' : '/';
    return result;
}

std::string base64_encoding(std::string text){
    std::string converted;
    converted += base64_mapping(text[0] >> 0b10);
    converted += base64_mapping((text[1] >> 0b100) | ((text[0] & 0b11) << 0b100));
    converted += base64_mapping((text[2] >> 0b110) | ((text[1] & 0b1111) << 0b10));
    converted += base64_mapping(text[2] & 0b111111);
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
    std::string temp, read, encoded;
    std::ifstream text (argv[1]);
    if(text.is_open()){
        while(!text.eof()){
            getline(text, temp);
            for(int i = 0; i < temp.size(); i++){
                read += temp[i];
                if(read.size() == 3 || i == temp.size()-1){
                    encoded += base64_encoding(read);
                    read = "";
                }
            }
            if(temp.size()%3)
                for(int i = 0; i < 3 - temp.size()%3; i++)
                    encoded[encoded.size()-1-i] = '=';
        }
        std::ofstream output ("encoded.txt");
        output << encoded;
        text.close();
        output.close();
    } else{
        std::cout << "Cannot open the text file :/" << std::endl;
        return -1;
    }
    return 0;
}