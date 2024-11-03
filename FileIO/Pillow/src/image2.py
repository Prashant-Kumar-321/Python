from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)


main()
