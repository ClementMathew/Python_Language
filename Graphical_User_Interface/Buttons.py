import tkinter as tk


class ButtonDemo(tk.Tk):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        super().__init__()

        # Set the title and initialize the main window
        self.title("Button Demo")

        # A single label in the first row
        self.label = tk.Label(self, text="Hello world!")
        self.label.grid(row=0, column=0, columnspan=2, sticky="NSEW")

        # Two command buttons in the second row
        self.clearBtn = tk.Button(self, text="Clear", command=self.clear_label)
        self.clearBtn.grid(row=1, column=0, sticky="NSEW")

        self.restoreBtn = tk.Button(
            self, text="Restore", state="disabled", command=self.restore_label
        )
        self.restoreBtn.grid(row=1, column=1, sticky="NSEW")

    def clear_label(self):
        """Clears the label's text and disables the Clear button, enables Restore."""
        self.label.config(text="")
        self.clearBtn.config(state="disabled")
        self.restoreBtn.config(state="normal")

    def restore_label(self):
        """Restores the label's text and enables the Clear button, disables Restore."""
        self.label.config(text="Hello world!")
        self.clearBtn.config(state="normal")
        self.restoreBtn.config(state="disabled")


# Main function to run the application
def main():
    app = ButtonDemo()
    app.mainloop()


if __name__ == "__main__":
    main()
