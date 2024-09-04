from PIL import Image

def grayscale(image):

    """Converts the argument image to grayscale."""

    for y in range(image.height):
        for x in range(image.width):

            # Get the pixel value (r, g, b)
            r, g, b = image.getpixel((x, y))
            
            # Calculate the luminance using the formula
            lum = int(r * 0.299 + g * 0.587 + b * 0.114)
            
            # Set the pixel to the new grayscale value
            image.putpixel((x, y), (lum, lum, lum))

def main(filename="image.png"):

    # Open the image file
    image = Image.open(filename)
    
    # Convert to RGB if the image is not in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert the image to grayscale
    grayscale(image)
    
    # Display the grayscale image
    image.show(title="Grayscale Image")
    
    # Optionally, save the grayscale image
    image.save("grayscale_" + filename)

if __name__ == "__main__":
    main()
