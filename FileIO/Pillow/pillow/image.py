from PIL import Image, ImageFilter
import os, sys,math


def main(): 
    with Image.open('./in.jpeg') as image:
        image = image.rotate(180)
        # width, height = image.size
        # scale_factor = 1.5
        # new_height = get_scaled_height(height, scale_factor)
        # new_width = get_scaled_width(width, scale_factor)
        # image = image.resize((new_width, new_height))

        # image = image.crop((50, 50, 1000, 700))

        # image = image.transpose(Image.TRANSPOSE)

        image.save("out.jpeg")


def get_filter(num): 
    match num: 
        case 1: return ImageFilter.BLUR
        case 2: return ImageFilter.CONTOUR
        case 3: return ImageFilter.DETAIL
        case 4: return ImageFilter.EDGE_ENHANCE
        case 5: return ImageFilter.EDGE_ENHANCE_MORE
        case 6: return ImageFilter.EMBOSS
        case 7: return ImageFilter.FIND_EDGES
        case 8: return ImageFilter.SHARPEN
        case 9: return ImageFilter.SMOOTH
        case 10: return ImageFilter.SMOOTH_MORE

def get_scaled_width(width, factor): 
    return int(round(width * factor, 0))

def get_scaled_height(height, factor): 
    return int(round(height * factor, 0))


def get_new_height(width, height, new_width): 
    return int(round(height/width * new_width, 0))

def get_new_width(width, height, new_height): 
    return int(round(width/height * new_height, 0))



if __name__=="__main__": 
    main()