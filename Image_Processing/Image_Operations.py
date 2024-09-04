from PIL import Image,ImageDraw

image = Image.open("image.png")

# width, height
width, height = image.size
print(f"Width: {width}")
print(f"Height: {height}")

# pixel value
x, y = 50, 100  
pixel_value = image.getpixel((x, y))
print(f"Pixel value at ({x}, {y}): {pixel_value}")

# Show the image
image.show()