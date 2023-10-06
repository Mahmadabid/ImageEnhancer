from PIL import Image
from uniquePath import generate_unique_filename

def upscale_image(input_path='img.jpg', output_path='scaled_image.jpg'):
    output_path = generate_unique_filename(output_path)
    """Upscale the image 4 times its original size."""
    # Load the original image
    img = Image.open(input_path)

    # Calculate new dimensions
    width, height = img.size
    new_width = width * 4
    new_height = height * 4

    # Scale the image
    scaled_img = img.resize((new_width, new_height), Image.NEAREST)

    # Save the scaled image
    scaled_img.save(output_path)

if __name__ == "__main__":
    upscale_image()