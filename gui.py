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

# Sort data menu function
def sort_data_menu():
    # Create a new window
    global sort_window
    sort_window = tk.Toplevel()

    # Create two buttons
    button1 = tk.Button(sort_window, text="Sort by Song Name", command=sort_song_name)
    button2 = tk.Button(sort_window, text="Sort by Artist Name", command=sort_artist_name)

    # Add the buttons to the window
    button1.pack()
    button2.pack()

#EXAMPLE DATA
music = [("Drake","God's plan","2018", 3.19),("ArtistB","SongB","2018", 3.19),("ArtistA","SongA","2015",2.54),("ArtistC","SongC","2017",3.24),("Future","Mask Off","2014",3.45)]
#EXAMPLE DATA

def output_sorted_data(list):
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END) #wipes console
    for item in list:
        output_text.insert(tk.END, str(item) + "\n")
    output_text.insert(tk.END, "Data sorted!\n")
    output_text.config(state=tk.DISABLED)

def sort_song_name():
    # Do something when the button is clicked
    sorted_music = sorted(music, key = lambda x: x[1])
    output_sorted_data(sorted_music)
    print("Sorting by song name...")
    # Close the window
    sort_window.destroy()

def sort_artist_name():
    # Do something when the button is clicked
    sorted_music = sorted(music, key = lambda x: x[0])
    output_sorted_data(sorted_music)
    print("Sorting by artist name...")
    # Close the window
    sort_window.destroy()

# Upload file function
def upload_file():
    file_path = filedialog.askopenfilename()
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Selected file: " + file_path + "\n")
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
upload_button_image = tk.PhotoImage(file="GUI_assets/upload.png")
upload_button = tk.Button(button_frame, image=upload_button_image, command=upload_file)
upload_button.pack(side=tk.LEFT)

# sort data menu button
sort_button_image = tk.PhotoImage(file="GUI_assets/sort.png")
sort_button = tk.Button(button_frame, image=sort_button_image, command=sort_data_menu)
sort_button.pack(side=tk.LEFT)

# refresh button
ping_button_image = tk.PhotoImage(file="GUI_assets/ping.png")
ping_button = tk.Button(button_frame, image=ping_button_image, command=ping_website)
ping_button.pack(side=tk.LEFT)

# start
root.mainloop()