from PIL import Image
from PIL import ImageFilter
import os 

def main(): 
    with Image.open('./in.jpeg') as image:
        image = image.rotate(180)
        image = image.filter(ImageFilter.FIND_EDGES)
        image.save("out.jpeg")



if __name__=="__main__": 
    main()