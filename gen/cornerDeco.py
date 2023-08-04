import PIL.Image                

image = PIL.Image.open("gen/input/topleft_fixed_resolution.png")
pixels = image.load()
width, height = image.size  

with open("gen/output/deco_fix.lua", "w") as f:    
    for y in range(height):         
        for x in range(width):
            print(f"({x}, {y}) = {pixels[x, y]}")
            if pixels[x, y] == 2:                
                f.write(f"paintutils.drawPixel({x + 2}, {y + 2}, colors.orange)\n")
                f.write(f"paintutils.drawPixel(width - {(x + 1)}, {y + 2}, colors.orange)\n")
                f.write(f"paintutils.drawPixel({(x + 2)}, height - {y + 1}, colors.orange)\n")
                f.write(f"paintutils.drawPixel(width - {(x + 1)}, height - {y + 1}, colors.orange)\n")
            elif pixels[x, y] == 1:
                f.write(f"paintutils.drawPixel({x + 2}, {y + 2}, colors.yellow)\n")
                f.write(f"paintutils.drawPixel(width - {(x + 1)}, {y + 2}, colors.yellow)\n")
                f.write(f"paintutils.drawPixel({(x + 2)}, height - {y + 1}, colors.yellow)\n")
                f.write(f"paintutils.drawPixel(width - {(x + 1)}, height - {y + 1}, colors.yellow)\n")
