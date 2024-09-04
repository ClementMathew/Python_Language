from PIL import Image

def black_and_white(image):

    """Converts the argument image to black and white."""

    black_pixel = (0, 0, 0)
    white_pixel = (255, 255, 255)
    
    # Convert the image to RGB if it's not already
    image = image.convert("RGB")
    pixels = image.load()  # Load pixel data

    for y in range(image.height):
        for x in range(image.width):

            r, g, b = pixels[x, y]
            average = (r + g + b) // 3
            
            if average < 128:
                pixels[x, y] = black_pixel
            else:
                pixels[x, y] = white_pixel
    
    return image

def main(filename="image.png"):

    image = Image.open(filename)
    
    bw_image = black_and_white(image)
    print("Close the image window to quit.")
    bw_image.show()

if __name__ == "__main__":
    main()
