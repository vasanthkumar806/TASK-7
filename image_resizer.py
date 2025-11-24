import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
NEW_SIZE = (800, 800)
OUTPUT_FORMAT = "JPEG"

def resize_images():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            img_path = os.path.join(INPUT_FOLDER, filename)
            img = Image.open(img_path)
            resized_img = img.resize(NEW_SIZE)
            new_name = os.path.splitext(filename)[0] + f".{OUTPUT_FORMAT.lower()}"
            output_path = os.path.join(OUTPUT_FOLDER, new_name)
            resized_img.save(output_path, OUTPUT_FORMAT)
            print(f"Saved: {output_path}")

    print("All images resized successfully!")

if __name__ == "__main__":
    resize_images()
