import tkinter as tk
from tkinter import ttk


class TextFieldDemo(tk.Tk):
    """Converts an input string to uppercase and displays the result."""

    def __init__(self):
        """Sets up the window and widgets."""
        super().__init__()

        self.title("Text Field Demo")

        # Label and field for the input
        input_label = ttk.Label(self, text="Input")
        input_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

        self.inputField = ttk.Entry(self)
        self.inputField.grid(row=0, column=1, padx=5, pady=5, sticky="EW")

        # Label and field for the output
        output_label = ttk.Label(self, text="Output")
        output_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

        self.outputField = ttk.Entry(self, state="readonly")
        self.outputField.grid(row=1, column=1, padx=5, pady=5, sticky="EW")

        # The command button
        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        convert_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Adjust column weights for resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

    def convert(self):
        """Inputs the string, converts it to uppercase, and outputs the result."""
        text = self.inputField.get()
        result = text.upper()
        self.outputField.config(state="normal")
        self.outputField.delete(0, tk.END)  # Clear the output field
        self.outputField.insert(0, result)
        self.outputField.config(state="readonly")


def main():
    app = TextFieldDemo()
    app.mainloop()


if __name__ == "__main__":
    main()
