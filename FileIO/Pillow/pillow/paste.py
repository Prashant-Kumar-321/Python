from PIL import Image, ImageOps

def main(): 
    with Image.open('./croped1.jpeg') as output_image, Image.open("./tomato.png") as input_image: 

        # Pasting a transparent background image on top of a solid background image

        # Ensure both images are in RGBA mode to support transparency
        # input_image = input_image.convert("RGBA")
        # output_image = output_image.convert("RGBA")

        output_image.paste(input_image, mask=input_image)

        output_image.save("./ocean-wave-tomato.jpeg")

if __name__ == "__main__": 
    main()