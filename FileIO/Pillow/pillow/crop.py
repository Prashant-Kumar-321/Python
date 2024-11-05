from PIL import Image, ImageOps

def main():
    with Image.open("./out.jpeg") as image:
        width, height = image.size 

        width = int(round(0.5 * width, 0))
        height = int(round(0.5 * height))

        image = ImageOps.fit(image,(width, height), centering=(0.5, 0.5))
        image.save("./croped.jpeg")


if __name__ == "__main__": 
    main()