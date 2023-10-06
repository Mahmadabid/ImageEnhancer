import os

def generate_unique_filename(filename):
    """
    Generates a unique filename by appending numbers if the file already exists.
    """
    base, ext = os.path.splitext(filename)
    counter = 1

    while os.path.exists(filename):
        filename = f"{base}_{counter}{ext}"
        counter += 1

    return filename
