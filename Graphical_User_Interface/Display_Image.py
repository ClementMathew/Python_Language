import tkinter as tk
from tkinter import PhotoImage
from tkinter.font import Font


class ImageDemo(tk.Tk):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and the widgets."""
        super().__init__()

        self.title("Image Demo")
        self.resizable(False, False)  # Disable window resizing

        # Add the image label
        self.imageLabel = tk.Label(self)
        self.imageLabel.grid(row=0, column=0, sticky="NSEW")

        # Add the text label
        self.textLabel = tk.Label(self, text="The Image")
        self.textLabel.grid(row=1, column=0, sticky="NSEW")

        # Load the image and associate it with the image label
        self.image = PhotoImage(file="image.png")
        self.imageLabel["image"] = self.image

        # Set the font and color of the caption
        font = Font(family="Verdana", size=20, slant="italic")
        self.textLabel["font"] = font
        self.textLabel["foreground"] = "blue"


# Main function to run the application
def main():
    app = ImageDemo()
    app.mainloop()


if __name__ == "__main__":
    main()
