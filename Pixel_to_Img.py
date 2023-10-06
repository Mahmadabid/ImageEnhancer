import re
from PIL import Image
from uniquePath import generate_unique_filename

def pixels_to_image(input_path='imgPixel.txt', output_path='output_image.jpg'):
    output_path = generate_unique_filename(output_path)
    """Convert pixel data from a text file to an image."""
    
    # Step 1: Read the file
    with open(input_path, 'r') as f:
        content = f.read()

    # Using regex to extract tuples
    pixel_strings = re.findall(r'\((\d+),\s*(\d+),\s*(\d+)\)', content)
    pixels = [(int(r), int(g), int(b)) for r, g, b in pixel_strings]

    # Assuming the image is square for simplicity
    image_size = int(len(pixels)**0.5)

    # Step 2: Generate the image
    img = Image.new('RGB', (image_size, image_size))
    img.putdata(pixels)
    img.save(output_path)

if __name__ == "__main__":
    pixels_to_image()