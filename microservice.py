import base64
import io
import os
import time
from PIL import Image
from rembg import remove

def process_image(input_path, output_path, flag_path):
    while True:
        # waiting for flag
        if os.path.exists(flag_path):
            print("Flag detected. Processing image...")

            with open(input_path, "r") as file:
                encoded_string = file.read()

            # decode image
            image_data = base64.b64decode(encoded_string)
            image = Image.open(io.BytesIO(image_data))

            # remove the background
            processed_data = remove(image)

            # save the processed image to a buffer
            buffer = io.BytesIO()
            processed_data.save(buffer, format="PNG")
            processed_image_data = buffer.getvalue()

            # encode the processed image to Base64
            processed_encoded = base64.b64encode(processed_image_data).decode("utf-8")

            # write to the output file
            with open(output_path, "w") as file:
                file.write(processed_encoded)

            print(f"Processed image saved to {output_path}")

            os.remove(input_path)
            os.remove(flag_path)

        time.sleep(1)

def main():
    process_image("image.txt", "processed_image.txt", "ready.flag")

if __name__ == "__main__":
    main()