# ImgEnhancerMicroservice
Microservice for Zach

To Request Data:
1. Convert image to a Base64 string and write it to a text file
2. Create a flag file to notify microservice to start
   
Example call: send_img(img_filename, "img.txt", "ready.flag")

Revision: Example of code I used to request data from the microservice

def send_image(file_path, output_path, flag_path):
    try:
        with open(file_path, "rb") as image_file:
            # convert the image to Base64 string
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            
        # write the encoded image to the text file
        with open(output_path, "w") as file:
            file.write(encoded_string)

        #  flag file to notify the microservice
        with open(flag_path, "w") as flag_file:
            flag_file.write("ready")

        print(f"Image '{file_path}' sent and flag set: {flag_path}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

To Recieve Data:
1. Once the microservice is done enhancing the image, it sends the data to the output text file
2. The main program should moniter this text file and convert the Base64 string back into an image
   
Example call: receive_img("processed_img.txt", "enhanced_clothing.png")

Revision: Example of code I used to recieve data from the microservice

def receive_image(input_path, output_path):
    print("Waiting for processed image...")
    while not os.path.exists(input_path):
        time.sleep(1)

    with open(input_path, "r") as file:
        encoded_string = file.read()

    # decode and save the processed image
    image_data = base64.b64decode(encoded_string)
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)

    print(f"Processed image saved to {output_path}")
    # os.remove(input_path)


![UML diagram](https://github.com/user-attachments/assets/ab8d7af5-daba-4474-a49e-2ea478365ab6)
