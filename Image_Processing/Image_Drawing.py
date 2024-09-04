from PIL import Image, ImageDraw

# Create a new blank image (250x250) with a white background
image = Image.new("RGB", (250, 250), "white")
draw = ImageDraw.Draw(image)

# Define the color blue
blue = (0, 0, 255)

# Calculate the y-coordinate for the middle of the image
y = image.height // 2

# Draw a horizontal line in the middle
for x in range(image.width):
    draw.point((x, y-1), fill=blue)  # just above the center
    draw.point((x, y), fill=blue)    # on the center line
    draw.point((x, y+1), fill=blue)  # just below the center

# Show the image
image.show()