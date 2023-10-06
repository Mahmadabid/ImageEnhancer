# Image Processing Tool

This repository contains an image processing toolkit that provides functionalities such as upscaling an image, converting pixel data to an image, and extracting pixel data from an image. Additionally, it provides a GUI-based application to interactively execute these operations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Files Description](#files-description)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Prerequisites

- Python (tested with version 3.x)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyQt5-tools](https://pypi.org/project/pyqt5-tools/)

## Setup

1. Clone this repository:

```ruby
git clone [https://github.com/Mahmadabid/ImageUpscaler]
```

2. Navigate to the project directory:

```ruby
cd ImageUpscaler
```

3. Install the required dependencies:

```ruby
pip install Pillow PyQt5 pyqt5-tools
```


## Usage

To utilize the GUI application:

```ruby
python Gui.py
```


Follow the on-screen instructions to select and execute the desired image processing operation.

### Individual Scripts



#### 1. Upscale an Image

   To upscale an image:

```ruby
python ImgUpscaler.py
```

    By default, it uses `img.jpg` as input and produces an upscaled image.



#### 2. Convert Pixel Data to Image

    To convert pixel data (from a text file) back to an image:

```ruby
python Pixel_to_Img.py
```

    By default, it uses `imgPixel.txt` as input and creates an image from the pixel data.



#### 3. Extract Pixel RGB Values from an Image

    To extract RGB values from an image and save to a text file:

```ruby
python Img_to_Pixel.py
```
    By default, it uses `img.jpg` as input and outputs the pixel RGB values to `imgPixel.txt`.



#### 4. Generating Unique Filenames with uniquePath.py

    The `uniquePath.py` script contains a utility function to ensure generated filenames are unique. While it's primarily integrated into the other scripts to avoid filename conflicts, advanced users can leverage this function in custom scripts or integrations.

    To utilize the unique filename generation in custom scripts:

Note: The default inputs and outputs can be changed within each script or modified to accept command line arguments based on user preference.

## Files Description

- `ImgUpscaler.py`: Upscales a sqaure image to 4x its original size.
- `Pixel_to_Img.py`: Converts pixel data from a text file back to an image.
- `Img_to_Pixel.py`: Extracts pixel RGB values from an image and saves them to a text file.
- `uniquePath.py`: Utility script that generates unique filenames.
- `Gui.py`: GUI application integrating all the above functionalities.
- `img.jpg`: Sample image file used for demonstrations and testing the toolkit's functionalities.
- `imgPixel.txt`: Sample text file that contains rows of pixel data. Each line in this file represents a list of RGB tuples corresponding to a row of pixels from the original image (e.g., `[(255, 255, 255), (0, 0, 0)]` where each tuple represents the RGB value of a pixel).
