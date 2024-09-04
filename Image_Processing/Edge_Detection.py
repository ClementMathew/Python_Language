from PIL import Image

def detectEdges(image, amount): 

    """Builds and returns a new image in which the edges of the argument image are highlighted and the colors are reduced to black and white."""
    
    def average(triple): 
        r, g, b = triple[:3]  # Ignore the alpha channel if it exists
        return (r + g + b) // 3

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new_image = image.copy()

    width, height = image.size

    for y in range(height - 1):
        for x in range(1, width):

            oldPixel = image.getpixel((x, y))
            leftPixel = image.getpixel((x - 1, y))
            bottomPixel = image.getpixel((x, y + 1))

            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)

            if abs(oldLum - leftLum) > amount or abs(oldLum - bottomLum) > amount:
                new_image.putpixel((x, y), blackPixel)
            else:
                new_image.putpixel((x, y), whitePixel)

    return new_image

# Example usage:
if __name__ == "__main__":

    # Load an image
    image = Image.open("image.png")  # Replace with the correct path

    # Detect edges with a specific threshold amount
    amount = 20  # Adjust this value to change edge sensitivity
    edge_image = detectEdges(image, amount)

    # Save the edge-detected image
    edge_image.save("edge_detected_image.png")

    # Show the edge-detected image
    edge_image.show()
