import tkinter as tk
from tkinter import ttk, messagebox
import math


class NumberFieldDemo(tk.Tk):
    """Computes and displays the square root of an input number."""

    def __init__(self):
        """Sets up the window and widgets."""
        super().__init__()

        self.title("Number Field Demo")

        # Label and field for the input
        input_label = ttk.Label(self, text="An integer:")
        input_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

        self.inputField = ttk.Entry(self)
        self.inputField.grid(row=0, column=1, padx=5, pady=5, sticky="EW")

        # Label and field for the output
        output_label = ttk.Label(self, text="Square root:")
        output_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

        self.outputField = ttk.Entry(self, state="readonly")
        self.outputField.grid(row=1, column=1, padx=5, pady=5, sticky="EW")

        # The command button
        compute_button = ttk.Button(self, text="Compute", command=self.computeSqrt)
        compute_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Adjust column weights for resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

    def computeSqrt(self):
        """Inputs the integer, computes the square root, and outputs the result. Handles input errors by displaying a message box."""
        try:
            number = int(self.inputField.get())
            if number < 0:
                raise ValueError("Input must be a non-negative integer.")
            result = math.sqrt(number)
            self.outputField.config(state="normal")
            self.outputField.delete(0, tk.END)  # Clear the output field
            self.outputField.insert(0, f"{result:.2f}")
            self.outputField.config(state="readonly")
        except ValueError as e:
            messagebox.showerror("ERROR", str(e))


def main():
    app = NumberFieldDemo()
    app.mainloop()


if __name__ == "__main__":
    main()
