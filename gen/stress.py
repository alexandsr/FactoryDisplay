import PIL.Image                
image = PIL.Image.open(f"gen/input/stress.png")
pixels = image.load()
width, height = image.size

with open(f"gen/output/stress.lua", "w") as f:    
    for y in range(height):         
        for x in range(width):
            print(f"({x}, {y}) = {pixels[x, y]}")
            if pixels[x, y] == 0 or pixels[x, y] == (0, 0, 0, 255):                
                f.write(f"paintutils.drawPixel({x-(0.5*width)} + (0.5*width) + 2, {y + 28}, colors.gray)\n")
            elif pixels[x, y] == 1 or pixels[x, y] == (128, 128, 128, 255):
                f.write(f"paintutils.drawPixel({x-(0.5*width)} + (0.5*width) + 2, {y + 28}, colors.lightGray)\n")
