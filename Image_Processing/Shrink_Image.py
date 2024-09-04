from PIL import Image

def shrink(image, factor):

    """Builds and returns a new image which is a smaller copy of the argument image, by the factor argument."""
    
    width, height = image.size
    new_width = width // factor
    new_height = height // factor
    new_image = Image.new("RGB", (new_width, new_height))
    
    for newY in range(new_height):
        for newX in range(new_width):
            oldX = newX * factor
            oldY = newY * factor
            old_pixel = image.getpixel((oldX, oldY))
            new_image.putpixel((newX, newY), old_pixel)
    
    return new_image

# Example usage:
if __name__ == "__main__":

    # Load an image
    image = Image.open("image.png")  # Replace with the actual image path

    # Shrink the image by a factor of 2
    factor = 2
    smaller_image = shrink(image, factor)

    # Save the smaller image
    smaller_image.save("smaller_image.jpg")

    # Show the smaller image
    smaller_image.show()
