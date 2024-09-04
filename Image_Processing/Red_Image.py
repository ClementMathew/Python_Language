from PIL import Image

# Create a new image with a red background (150x150)
image = Image.new("RGB", (150, 150), (255, 0, 0))

# Show the image
image.show()
