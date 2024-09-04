from PIL import Image

# Load the image
image = Image.open("image.png")

# Display the original image
image.show(title="Original Image")

# Clone the image
newImage = image.copy()

# Display the cloned image
newImage.show(title="Cloned Image")

