import tkinter as tk
from tkinter import messagebox

def validate_input():
    input_value = entry.get()

    if not input_value.isdigit():
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    # If the input is a valid number, process it here
    # For example, you can convert the input to an integer and perform some calculations
    try:
        input_number = int(input_value)
        result_label.config(text=f"Result: {input_number * 2}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input: Not a valid integer.")

root = tk.Tk()
root.title("Input Validation Example")

entry = tk.Entry(root)
entry.pack(pady=10)

validate_button = tk.Button(root, text="Validate", command=validate_input)
validate_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
