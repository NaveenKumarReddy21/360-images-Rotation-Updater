import json
import tkinter as tk
from tkinter import filedialog, messagebox

def update_rotation_in_json(file_path, new_rotation):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        def update_rotation(obj):
            if isinstance(obj, dict):
                for key in obj:
                    if key.lower() == 'rotation' and isinstance(obj[key], list):
                        obj[key] = new_rotation
                    else:
                        update_rotation(obj[key])
            elif isinstance(obj, list):
                for item in obj:
                    update_rotation(item)

        update_rotation(data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Success", "Rotation values updated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select images.json", 
        filetypes=[("JSON files", "images.json")]
    )
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def apply_changes():
    file_path = file_entry.get()
    try:
        new_rotation = [float(x_entry.get()), float(y_entry.get()), float(z_entry.get())]
        update_rotation_in_json(file_path, new_rotation)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for X, Y, and Z rotations.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Rotation Updater v1.0.0 by Naveen Kumar Reddy")
root.geometry("500x300")
root.resizable(False, False)

# File selection row
tk.Label(root, text="JSON File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5)

# Rotation input fields
tk.Label(root, text="Rotation X:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
x_entry = tk.Entry(root, width=30)
x_entry.grid(row=1, column=1, sticky="w")

tk.Label(root, text="Rotation Y:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
y_entry = tk.Entry(root, width=30)
y_entry.grid(row=2, column=1, sticky="w")

tk.Label(root, text="Rotation Z:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
z_entry = tk.Entry(root, width=30)
z_entry.grid(row=3, column=1, sticky="w")

# Apply button
tk.Button(root, text="Apply Rotation", command=apply_changes, bg="lightblue").grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()
