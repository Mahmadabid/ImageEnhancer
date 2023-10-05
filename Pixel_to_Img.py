import re
from PIL import Image

# Step 1: Read the file
with open('imgPixel.txt', 'r') as f:
    content = f.read()

# Using regex to extract tuples
pixel_strings = re.findall(r'\((\d+),\s*(\d+),\s*(\d+)\)', content)
pixels = [(int(r), int(g), int(b)) for r, g, b in pixel_strings]

# Assuming the image is square for simplicity
image_size = int(len(pixels)**0.5)

# Step 2: Generate the image
img = Image.new('RGB', (image_size, image_size))
img.putdata(pixels)
img.save('output_image.jpg')
