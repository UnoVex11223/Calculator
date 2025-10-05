import tkinter as tk


class Calculator:
    """
    A simple calculator application built using tkinter.
    """

    def __init__(self, bg_color):
        """Initializes the calculator window and its components."""
        # Initializes the main application window (Tk object)
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Configures the background color of the main window
        self.root.config(bg=bg_color)

        # Stores the background color for use in subordinate widgets
        self.app_color = bg_color

        # --- MODIFICATION 1: Set a maximum length for the display ---
        self.MAX_DISPLAY_LENGTH = 15

        # Create the Display Box
        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.display_box = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 28, 'bold'),
            bd=15,
            relief="sunken",
            justify="right",
            bg='#ffffff',
            fg='#333333',
            insertbackground='#333333'
        )
        self.display_box.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Creates a container Frame for buttons
        self.button_frame = tk.Frame(self.root, bg=self.app_color, bd=5, relief='raised')
        self.button_frame.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)

        # Calls the method that creates and lays out all the buttons
        self.create_buttons()

        # Configuration for resizing:
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Configure button_frame columns and rows to expand
        for i in range(5):
            self.button_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_rowconfigure(i, weight=1)

    def button_click(self, value):
        """Appends the clicked number or operator value to the display string."""
        current_text = self.display_var.get()

        # --- MODIFICATION 2: Prevent more input if display is full ---
        if len(current_text) >= self.MAX_DISPLAY_LENGTH:
            return  # Stop the function if the limit is reached

        # Logic to handle leading zeros
        if current_text == "0" and str(value).isdigit():
            new_text = str(value)
        elif current_text == "" and str(value) == "0":
            new_text = "0"
        else:
            new_text = current_text + str(value)

        self.display_var.set(new_text)

    def clear_display(self):
        """Clears the display to an empty string."""
        self.display_var.set("")

    def evaluate(self):
        """Calculates the result of the expression in the display using eval()."""
        try:
            expression = self.display_var.get()
            result = str(eval(expression))

            # Truncate long results before displaying
            if len(result) > self.MAX_DISPLAY_LENGTH:
                # You might want to display an error or use scientific notation for very long results
                result = "Error: Too long"

            self.display_var.set(result)

        except (SyntaxError, ZeroDivisionError, NameError):
            self.display_var.set("Error")
        except Exception:
            self.display_var.set("Error")

    def create_buttons(self):
        """Creates and lays out all the buttons in the button_frame."""
        # Define common button styling
        button_style = {
            'font': ("Arial", 16, 'bold'),
            'width': 5,
            'height': 2,
            'bd': 4,
            'relief': 'raised',
            'fg': '#333333',
            'bg': '#ffffff',
            'activebackground': '#cccccc',
            'activeforeground': '#000000',
            'padx': 5,
            'pady': 5
        }

        # --- MODIFICATION 3: Create a new style for grey operator/equals buttons ---
        grey_button_style = button_style.copy()
        grey_button_style['bg'] = '#c0c0c0'  # Silver grey
        grey_button_style['fg'] = 'black'
        grey_button_style['activebackground'] = '#a9a9a9'  # Darker grey for active state

        # Creates the number buttons (1-9)
        for r in range(3):
            for c in range(3):
                button_value = r * 3 + c + 1
                tk.Button(
                    self.button_frame,
                    text=f"{button_value}",
                    command=lambda v=button_value: self.button_click(v),
                    **button_style
                ).grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        # Creates the '0' button
        tk.Button(
            self.button_frame,
            text="0",
            command=lambda v=0: self.button_click(v),
            **button_style
        ).grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

        # Creates operator buttons using the new grey style
        tk.Button(self.button_frame, text="+", command=lambda v='+': self.button_click(v), **grey_button_style).grid(
            row=0, column=4, sticky="nsew", padx=2, pady=2)
        tk.Button(self.button_frame, text="-", command=lambda v='-': self.button_click(v), **grey_button_style).grid(
            row=1, column=4, sticky="nsew", padx=2, pady=2)
        tk.Button(self.button_frame, text="*", command=lambda v='*': self.button_click(v), **grey_button_style).grid(
            row=2, column=4, sticky="nsew", padx=2, pady=2)
        tk.Button(self.button_frame, text="/", command=lambda v='/': self.button_click(v), **grey_button_style).grid(
            row=3, column=4, sticky="nsew", padx=2, pady=2)

        # Creates the "Clear" button with its own style
        clear_style = button_style.copy()
        clear_style['bg'] = '#ff6961'  # A soft red for clear/delete
        clear_style['fg'] = 'white'
        clear_style['activebackground'] = '#e05a53'

        tk.Button(
            self.button_frame,
            text="Clear",
            command=self.clear_display,
            **clear_style
        ).grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

        # Creates the "=" button using the new grey style
        tk.Button(
            self.button_frame,
            text="=",
            command=self.evaluate,
            **grey_button_style
        ).grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

    def run(self):
        """Starts the main tkinter event loop."""
        self.root.mainloop()