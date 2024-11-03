import csv, numpy as np
from PIL import Image

def main(): 
    with open('./views.csv') as view, open('./p_analysis.csv', "w") as analysis: 
        reader = csv.DictReader(view)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames+['brightness'])
        writer.writeheader()

        for row in reader: 
            filename = f'./{row["id"]}.jpeg'
            try: 
                row['brightness']  = round(calculate_brightness(filename), 2)
            except FileNotFoundError: 
                continue 

            writer.writerow(row)

def calculate_brightness(filename): 
    try: 
        with Image.open(filename) as image: 
            array = np.array(image.convert("L"))
            avg_brightness = np.mean(array) / 255
        return avg_brightness
    
    except FileNotFoundError: 
        raise FileNotFoundError("Specified image file was not found at the specified location")

if __name__ == "__main__": 
    main()