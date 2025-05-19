import base64
import os
import time

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
    os.remove(input_path)

def main():
    # Prompt the user to enter the image filename
    image_filename = input("Enter the image filename: ").strip()

    # Check if the file exists
    if not os.path.exists(image_filename):
        print(f"Error: '{image_filename}' not found in the directory.")
        return

    # Send and receive the image
    send_image(image_filename, "image.txt", "ready.flag")
    receive_image("processed_image.txt", "enhanced_clothing.png")

if __name__ == "__main__":
    main()