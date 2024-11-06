from PIL import Image

def main(): 
    with Image.open('ocean_wave.jpeg') as bg, Image.open('cloud.png') as overlay: 
        
        bg = bg.convert("RGBA")
        overlay = overlay.convert("RGBA")

        bg.paste(overlay, (412, 0, 1052, 360), overlay)

        bg = bg.convert("RGB")

        bg.save("final.jpeg", "JPEG")

if __name__ == "__main__": 
    main()