from PIL import Image
from functools import reduce

def blur(image): 
    """Builds and returns a new image which is a blurred copy of the argument image."""

    def tripleSum(triple1, triple2):

        if len(triple1) == 1:  # Grayscale image
            return (triple1[0] + triple2[0],)

        else:  # RGB or RGBA image
            (r1, g1, b1) = triple1[:3]
            (r2, g2, b2) = triple2[:3]
            return (r1 + r2, g1 + g2, b1 + b2)

    new_image = image.copy()
    width, height = image.size

    for y in range(1, height - 1):
        for x in range(1, width - 1):

            oldP = image.getpixel((x, y))
            left = image.getpixel((x - 1, y))
            right = image.getpixel((x + 1, y))
            top = image.getpixel((x, y - 1))
            bottom = image.getpixel((x, y + 1))
            sums = reduce(tripleSum, [oldP, left, right, top, bottom])

            averages = tuple(map(lambda v: v // 5, sums))

            new_image.putpixel((x, y), averages)
    
    return new_image

# Example usage
if __name__ == "__main__":
    # Load an image

    image = Image.open("image.png")  # Assume this is an RGBA image
    
    # Apply the blur function
    blurred_image = blur(image)

    # Convert the image to RGB if it's in RGBA mode
    if blurred_image.mode == "RGBA":
        blurred_image = blurred_image.convert("RGB")

    # Save the blurred image as a JPEG
    blurred_image.save("blurred_image.jpg")

    # Show the blurred image
    blurred_image.show()
