from PIL import Image


def main():
    img = Image.open("in.jpeg")
    img.close()


main()
