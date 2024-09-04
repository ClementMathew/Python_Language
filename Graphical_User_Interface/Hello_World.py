import tkinter as tk

class LabelDemo(tk.Tk):
    """Displays a greeting in a window."""

    def __init__(self):
        super().__init__()
        self.title("Label Demo")
        label = tk.Label(self, text="Hello world!")
        label.pack()

def main():
    """Instantiates and pops up the window."""
    app = LabelDemo()
    app.mainloop()

if __name__ == "__main__":
    main()
