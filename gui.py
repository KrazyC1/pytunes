import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Window creation
root = tk.Tk()
root.title("Pytunes")

# Window size
root.geometry("675x450")

# Label for the output field
output_label = tk.Label(root, text="Output:", font=("Arial", 20))
output_label.pack()

# Output field
output_text = tk.Text(root, font=("Arial", 20), height=10)
output_text.config(state=tk.DISABLED)
output_text.pack()

# Upload file function
def upload_file():
    file_path = filedialog.askopenfilename()
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Selected file: " + file_path + "\n")
    output_text.config(state=tk.DISABLED)

# Sort data function
def sort_data():
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Data sorted!\n")
    output_text.config(state=tk.DISABLED)

# Ping / refresh function
def ping_website():
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Refreshing Data...\n")
    output_text.config(state=tk.DISABLED)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# upload file button
upload_button_image = tk.PhotoImage(file="upload.png")
upload_button = tk.Button(button_frame, image=upload_button_image, command=upload_file)
upload_button.pack(side=tk.LEFT)

# sort data button
sort_button_image = tk.PhotoImage(file="sort.png")
sort_button = tk.Button(button_frame, image=sort_button_image, command=sort_data)
sort_button.pack(side=tk.LEFT)

# refresh button
ping_button_image = tk.PhotoImage(file="ping.png")
ping_button = tk.Button(button_frame, image=ping_button_image, command=ping_website)
ping_button.pack(side=tk.LEFT)

# start
root.mainloop()
