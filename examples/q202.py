import tkinter as tk

def greet_user():
    name = entry.get()
    if name.strip() != '':
        label.config(text=f"Hello, {name}!")
    else:
        label.config(text="Please enter your name.")

root = tk.Tk()
root.title("Greetings App")
root.geometry("300x200")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=greet_user)
button.pack(pady=5)

root.mainloop()
