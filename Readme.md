# Image Processing Repository

This repository contains Python scripts for various image processing tasks including pixel extraction and image enhancement.

## 📄 Files and Descriptions


## Img_to_pixel.py

Converts a square image (`img.jpg`) into a list of pixel data. This pixel data is saved to `imgPixel.txt`.

**Usage:** 
```ruby
python Img_to_pixel.py
```

---

## `Pixel_to_Img.py`

Takes pixel data from `imgPixel.txt` and reconstructs it into an image. The resulting image is saved as `output_image.jpg`.

**Usage:** 
```ruby
python Pixel_to_Img.py
```

---

## `ImgEnhancer.py`

Enhances the resolution of an image by scaling it to four times its original dimensions.

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
