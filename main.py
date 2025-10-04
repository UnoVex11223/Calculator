import tkinter as tk


class Calculator:
    """
    A simple calculator application built using tkinter.
    """

    def __init__(self):
        # 1. Initialize the Main Window
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x500")

        # 2. Create the Display Box (Instance variables start with self.)
        self.display_var = tk.StringVar()
        self.display_box = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 20),
            bd=10,
            relief="sunken",
            justify="right"
        )
        # Layout the display
        self.display_box.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # 3. Create a frame to hold all the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0)

        # --- Button Creation Logic ---
        self.create_buttons()

        # 4. Configure Grid Weights for Resizing
        self.root.grid_rowconfigure(0, weight=0)  # Display row doesn't grow
        self.root.grid_rowconfigure(1, weight=1)  # Button row takes vertical space
        self.root.grid_columnconfigure(0, weight=1)  # Column expands horizontally

        # Note: You'll add event handling methods (e.g., self.button_click) here later

    def create_buttons(self):
        # Create the 3x3 grid of number buttons inside the frame
        for row in range(3):
            for col in range(3):
                button_value = row * 3 + col + 1
                tk.Button(
                    self.button_frame,
                    text=f"{button_value}",
                    width=10,
                    height=5,
                    # command=lambda v=button_value: self.button_click(v) # Future integration
                ).grid(row=row, column=col)

        # Row 3 (the 0 and the equals button)
        tk.Button(self.button_frame, text="0", width=10, height=5).grid(row=3, column=1)

        # Creates operation buttons (starts at column 4 in your original layout)
        tk.Button(self.button_frame, text="+", width=10, height=5).grid(row=0, column=4)
        tk.Button(self.button_frame, text="-", width=10, height=5).grid(row=1, column=4)
        tk.Button(self.button_frame, text="*", width=10, height=5).grid(row=2, column=4)
        tk.Button(self.button_frame, text="/", width=10, height=5).grid(row=3, column=4)

        # Button to clear calculator output window (spans two columns)
        tk.Button(
            self.button_frame,
            text="Clear",
            height=5,
            # command=self.clear_display # Future integration
        ).grid(row=3, column=0, columnspan=2, sticky="ew")

        # Creates button to evaluate values
        tk.Button(
            self.button_frame,
            text="=",
            width=10,
            height=5,
            # command=self.evaluate # Future integration
        ).grid(row=3, column=2)

    def run(self):
        """Starts the main tkinter event loop."""
        self.root.mainloop()


# --- Main execution block ---
if __name__ == "__main__":
    # Create an instance of the Calculator class
    calc_app = Calculator()
    # Start the application main loop
    calc_app.run()