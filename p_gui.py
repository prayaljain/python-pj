print("Khyati")
import tkinter as tk
from tkinter import messagebox
import math

# Function to calculate hypotenuse
def calculate_hypotenuse():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = math.sqrt(a**2 + b**2)
        result_label.config(text=f"Hypotenuse (c) = {c:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Pythagoras Theorem Calculator")
root.geometry("300x250")

# Title label
title = tk.Label(root, text="Pythagoras Theorem", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input fields for side a
label_a = tk.Label(root, text="Enter side a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

# Input fields for side b
label_b = tk.Label(root, text="Enter side b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

# Button to calculate
calc_button = tk.Button(root, text="Calculate Hypotenuse", command=calculate_hypotenuse)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Start the GUI event loop
root.mainloop()
