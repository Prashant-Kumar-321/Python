from PIL import Image


def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img.save("out.jpeg")
        

main()
