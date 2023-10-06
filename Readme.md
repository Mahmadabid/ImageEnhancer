# Image Processing Tool

This repository offers an image processing toolkit with features like upscaling images, converting pixel data to images, and extracting pixel data from images. It also provides an interactive GUI application to simplify these operations.

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
git clone https://github.com/Mahmadabid/ImageUpscaler
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

To use the GUI application:

```ruby
python Gui.py
```

Follow the on-screen prompts to select and perform the desired image processing task.

### Individual Scripts

#### 1. Upscale an Image

To upscale an image:

```ruby
python ImgUpscaler.py
```

By default, it processes `img.jpg` and generates an upscaled image.

#### 2. Convert Pixel Data to Image

To convert pixel data from a text file to an image:

```ruby
python Pixel_to_Img.py
```

This defaults to `imgPixel.txt` as input and produces an image from the pixel data.

#### 3. Extract Pixel RGB Values from an Image

To extract RGB values from an image and save them to a text file:

```ruby
python Img_to_Pixel.py
```

By default, it uses `img.jpg` for input and writes the pixel RGB values to `imgPixel.txt`.

#### 4. Generate Unique Filenames with `uniquePath.py`

This script ensures filename uniqueness. It's especially valuable when the other scripts are used independently without the GUI to prevent filename conflicts. Advanced users can also integrate its function in custom scripts or workflows.

> Note: The default file inputs and outputs can be adjusted in each script or configured to use command-line arguments based on user preference.

## Files Description

- `ImgUpscaler.py`: Upscales a square image to 4x its original size.
- `Pixel_to_Img.py`: Transforms pixel data from a text file back into an image.
- `Img_to_Pixel.py`: Extracts pixel RGB values from an image and writes them to a text file.
- `uniquePath.py`: Utility script that ensures unique filenames.
- `Gui.py`: GUI app that encompasses the functionalities of the above scripts.
- `img.jpg`: A sample image for testing and demonstration.
- `imgPixel.txt`: A sample text file containing rows of pixel data. Each line in the file represents a list of RGB tuples corresponding to a row of pixels from the source image, e.g., `[(255, 255, 255), (0, 0, 0)]`.