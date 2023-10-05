# Image Processing Repository

This repository contains Python scripts for various image processing tasks including pixel extraction and image enhancement.

## 📄 Files and Descriptions


## `Img_to_pixel.py`

**Purpose**: This script is designed to process square images. It extracts the pixel information from an input image, `img.jpg`, and saves this pixel data into a text file.

**Output**: A text file named `imgPixel.txt` containing a list of pixel RGB values derived from `img.jpg`.

**Usage:** 
```ruby
python Img_to_pixel.py
```

---

## `Pixel_to_Img.py`

**Purpose**: This script is dedicated to reconstructing images from pixel data. It reads pixel RGB values from a text file and forms an image out of them.

**Input**: Pixel data from `imgPixel.txt`.

**Output**: An image file named `output_image.jpg` reconstructed from the provided pixel data.

**Usage:** 
```ruby
python Pixel_to_Img.py
```

---

## `ImgEnhancer.py`

**Purpose**: The main goal of this script is image enhancement through size scaling. It processes an image and increases its size to four times its original dimensions.

**Output**: A scaled image that's 4x the size of the input image.

**Usage:** 
```ruby
python ImgEnhancer.py
```

---

## 🛠 Dependencies

* Python 3.x
* Pillow library

To install the required dependencies:
```ruby
pip install Pillow
```

# Write the content to README.md
```ruby
with open("README.md", "w") as f:
    f.write(readme_content)
```
