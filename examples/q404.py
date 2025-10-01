import tkinter as tk
import re

def validate_email(entry_value):
    # Regular expression pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the entered value matches the email pattern
    if re.match(email_pattern, entry_value):
        return True
    else:
        return False

def check_email():
    # Get the input from the Entry widget
    email = email_entry.get()

    # Validate the email using the validate_email function
    if validate_email(email):
        result_label.config(text="Valid email address", fg="green")
    else:
        result_label.config(text="Invalid email address", fg="red")

# Create the main Tkinter window
root = tk.Tk()
root.title("Email Validation")

# Create an Entry widget for entering the email
email_entry = tk.Entry(root)
email_entry.pack(pady=10)

# Create a button to validate the email
validate_button = tk.Button(root, text="Validate Email", command=check_email)
validate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", fg="black")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
