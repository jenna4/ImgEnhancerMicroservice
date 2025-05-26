# ImgEnhancerMicroservice
Microservice for Zach

To Request Data:
1. Convert image to a Base64 string and write it to a text file
2. Create a flag file to notify microservice to start
Example call: send_img(img_filename, "img.txt", "ready.flag")

To Recieve Data:
1. Once the microservice is done enhancing the image, it sends the data to the output text file
2. The main program should moniter this text file and convert the Base64 string back into an image
Example call: receive_img("processed_img.txt", "enhanced_clothing.png")


![UML diagram](https://github.com/user-attachments/assets/ab8d7af5-daba-4474-a49e-2ea478365ab6)
