import tkinter as tk

class LayoutDemo(tk.Tk):
    """Displays labels in the quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        super().__init__()

        # Adding labels to the window
        label1 = tk.Label(self, text="(0, 0)")
        label1.grid(row=0, column=0,sticky="NSEW")

        label2 = tk.Label(self, text="(0, 1)")
        label2.grid(row=0, column=1)

        label3 = tk.Label(self, text="(1, 0 and 1)")
        label3.grid(row=1, column=0,columnspan=2)

def main():
    """Instantiates and pops up the window."""
    app = LayoutDemo()
    app.title("Layout Demo")
    app.mainloop()

if __name__ == "__main__":
    main()
