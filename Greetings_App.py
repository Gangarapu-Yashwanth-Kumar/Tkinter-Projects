import tkinter as tk
from tkinter import messagebox

#Create the main window
root = tk.Tk() 
root.title("Greeting App")
root.geometry("300x200") # Set the window size
# Function to display a greeting message
def greet():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")
# Create a label
name_label = tk.Label(root, text="Enter your name:")
name_label.pack(pady=10) # Add some padding around the label
# Create an entry widget for user input
name_entry = tk.Entry(root)
name_entry.pack(pady=10) # Add some padding around the entry
# Create a button that triggers the greet function
button = tk.Button(root, text="Greet", command=greet)
button.pack(pady=20) # Add some padding around the button   
# Start the main event loop
root.mainloop()