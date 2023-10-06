from PIL import Image
from uniquePath import generate_unique_filename

def extract_pixel_colors(image_path="img.jpg"):
    """Extract RGB values of pixels from the provided image."""
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    width, height = img.size
    pixel_colors = []

    for y in range(height):
        row = []
        for x in range(width):
            color = pixels[y * width + x]
            row.append(color)
        pixel_colors.append(row)

    return pixel_colors

def save_pixel_colors_to_file(image_path="img.jpg", output_path="imgPixel.txt"):
    output_path = generate_unique_filename(output_path)
    """Save pixel RGB values from an image to a text file."""
    pixel_colors = extract_pixel_colors(image_path)

    with open(output_path, "w") as f:
        for row in pixel_colors:
            f.write(str(row) + "\n")

if __name__ == "__main__":
    save_pixel_colors_to_file()