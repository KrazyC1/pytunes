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

# Sorts music alphabetically based on artist or title of song 
def sortMusic(music, sortBy):
    if sortBy ==  "artistName":
        sorted_music = sorted(music, key = lambda x: x[0])
        return sorted_music
    elif sortBy == "songName":
        sorted_music = sorted(music, key = lambda x: x[1])
        return sorted_music

# Sort data function
def sort_data():
    #sample data
    music = [("Drake","God's plan","2018", 3.19),("ArtistB","SongB","2018", 3.19),("ArtistA","SongA","2015",2.54),("ArtistC","SongC","2017",3.24),("Future","Mask Off","2014",3.45)]

    secondary_window = tk.Toplevel()
    secondary_window.title("Sort By?")
    secondary_window.config(width=300, height=200)
    # Create a button to close (destroy) this window.
    button_song_name = ttk.Button(
        secondary_window,
        text="Close window",
        command=secondary_window.destroy
        sorted_music = sortMusic(music, "songName")
        output_text.insert(tk.END, sorted_music,"Data sorted!\n")
        output_text.config(state=tk.DISABLED)
    )
    button_song_name.place(x=0, y=0)

    button_artist_name = ttk.Button(
        secondary_window
        text="Sort by Artist Name"
        command=secondary_window.destroy
        output_text.config(state=tk.NORMAL)
        # variable holds list of sorted music
        sorted_music = sortMusic(music, "artistName")
        output_text.insert(tk.END, sorted_music,"Data sorted!\n")
        output_text.config(state=tk.DISABLED)
    )
    button_artist_name.place(x=0, y=25)

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