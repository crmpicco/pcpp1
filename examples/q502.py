import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    try:
        with open(file_path, 'r') as file:
            print("File opened successfully.")
    except FileNotFoundError:
        print("File not found. Please select a valid file.")
    except IOError as e:
        print(f"An error occurred while opening the file: {e}")

root = tk.Tk()

button = tk.Button(root, text="Open File", command=open_file)
button.pack()

root.mainloop()
