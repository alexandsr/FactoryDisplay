import PIL.Image                

image = PIL.Image.open("../image/left.png")
pixels = image.load()
width, height = image.size  

with open("scripts/left.lua", "w") as f:    
    for y in range(height):         
        for x in range(width):
            if pixels[x, y] == (0, 0, 0):  # Black pixel                  
                f.write(f"drawPixel({x}, {y}, colors.orange)\n")