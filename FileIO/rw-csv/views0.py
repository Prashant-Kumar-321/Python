import numpy as np
from PIL import Image


def main(): 
    print('Average brightness = ', calculate_brightness('./1.jpeg'))


def calculate_brightness(filename):
    with Image.open(filename) as image:
        array = np.array(image.convert("L"))
        brightness = np.mean(array) / 255
    return brightness


if __name__ == "__main__":
    main()
