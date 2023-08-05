import PIL.Image                

image = PIL.Image.open("gen/input/topleft_fixed_resolution.png")
pixels = image.load()
width, height = image.size  

with open("gen/output/deco_fix.lua", "w") as f:
    yValuesOrange = []
    xValuesOrange = []
    yValuesYellow = []
    xValuesYellow = []
    for y in range(height):         
        for x in range(width):
            print(f"({x}, {y}) = {pixels[x, y]}")
            if pixels[x, y] == 2:           
                xValuesOrange.append(x)
                yValuesOrange.append(y)
                # f.write(f"paintutils.drawPixel({x + 2}, {y + 2}, colors.orange)\n")
                # f.write(f"paintutils.drawPixel(width - {(x + 1)}, {y + 2}, colors.orange)\n")
                # f.write(f"paintutils.drawPixel({(x + 2)}, height - {y + 1}, colors.orange)\n")
                # f.write(f"paintutils.drawPixel(width - {(x + 1)}, height - {y + 1}, colors.orange)\n")
            elif pixels[x, y] == 1:
                xValuesYellow.append(x)
                yValuesYellow.append(y)
                # f.write(f"paintutils.drawPixel({x + 2}, {y + 2}, colors.yellow)\n")
                # f.write(f"paintutils.drawPixel(width - {(x + 1)}, {y + 2}, colors.yellow)\n")
                # f.write(f"paintutils.drawPixel({(x + 2)}, height - {y + 1}, colors.yellow)\n")
                # f.write(f"paintutils.drawPixel(width - {(x + 1)}, height - {y + 1}, colors.yellow)\n")
    f.write(f"xValuesDecoOrange = {{ {', '.join(map(str, xValuesOrange))[1:-1]} }}\n")
    f.write(f"yValuesDecoOrange = {{ {', '.join(map(str, yValuesOrange))[1:-1]} }}\n")
    f.write(f"xValuesDecoYellow = {{ {', '.join(map(str, xValuesYellow))[1:-1]} }}\n")
    f.write(f"yValuesDecoYellow = {{ {', '.join(map(str, yValuesYellow))[1:-1]} }}\n")