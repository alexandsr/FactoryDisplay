import PIL.Image                
images = ["anime", "componentPlant", "foodProcessing", "resourcePlant", "mainPlant"]
for value in images:
    image = PIL.Image.open(f"gen/input/{value}.png")
    pixels = image.load()
    width, height = image.size

    with open(f"gen/output/text/text_{value}.lua", "w") as f:    
        for y in range(height):         
            for x in range(width):
                if value == "componentPlant":
                    print(f"({x}, {y}) = {pixels[x, y]}")
                if pixels[x, y] == 0 or pixels[x, y] == (0, 0, 0, 255):                
                    f.write(f"paintutils.drawPixel({x-(0.5*width)} + (0.5*width) + 2, {y + 6}, colors.white)\n")
                elif pixels[x, y] == 1 or pixels[x, y] == (128, 128, 128, 255):
                    f.write(f"paintutils.drawPixel({x-(0.5*width)} + (0.5*width) + 2, {y + 6}, colors.gray)\n")
