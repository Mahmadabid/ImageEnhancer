from PIL import Image

def extract_pixel_colors(image_path):
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

image_path = "img.jpg"
pixel_colors = extract_pixel_colors(image_path)

f = open("imgPixel.txt", "w")

# To print the pixel colors:
for row in pixel_colors:
    f.write(str(row))
