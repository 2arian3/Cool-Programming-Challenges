# Base64
In computer science, Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding. Each Base64 digit represents exactly 6 bits of data. Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by four 6-bit Base64 digits.
Common to all binary-to-text encoding schemes, Base64 is designed to carry data stored in binary formats across channels that only reliably support text content. Base64 is particularly prevalent on the World Wide Web where its uses include the ability to embed image files or other binary assets inside textual assets such as HTML and CSS files.[wikipedia]<br>
## How to use?
**In order to use this simple program you should git clone this repository to your PC and enter the following commands in your terminal.**

### Encoder
If you have a text file and you want it to be converted to base64 enter this command.
```
./encode textFileName.txt
```
The result will be stored in **encoded.txt** in the same directory.

### Decoder
If you have a base64 file and you want it to be converted to simple text file enter this command.
```
./decode base64FileName.txt
```
The result will be stored in **decoded.txt** in the same directory.