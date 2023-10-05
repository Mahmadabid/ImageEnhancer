from PIL import Image

# Load the original image
img = Image.open('output_image.jpg')

# Scale the image
scaled_img = img.resize((2000, 2000), Image.NEAREST)

# Save the scaled image
scaled_img.save('scaled_image.jpg')
