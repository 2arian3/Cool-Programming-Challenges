#include <iostream>

char base64_mapping(int binary){
    char result = binary < 26 ? binary + 'A' :
                  binary < 52 ? binary + 'a' - 26 :
                  binary < 62 ? binary + '0' - 52 :
                  binary == 62 ? '+' : '/';
    return result;
}

std::string base64_encoding(std::string text){
    std::string converted;
    converted += base64_mapping(text[0] >> 2);
    converted += base64_mapping((text[1] >> 4) | ((text[0] & 3) << 4));
    converted += base64_mapping((text[2] >> 6) | ((text[1] & 15) << 2));
    converted += base64_mapping(text[2] & 63);
    return converted;
}

int main() {
    
}
