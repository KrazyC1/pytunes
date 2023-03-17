import tkinter as tk
import mp3
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
    """A function for the sort data menu."""
    # Create a new window
    global sort_window
    sort_window = tk.Toplevel()

    # Create two buttons
    button1 = tk.Button(sort_window, text="Sort by Song Name", command=sort_song_name)
    button2 = tk.Button(sort_window, text="Sort by Artist Name", command=sort_artist_name)
    button3 = tk.Button(sort_window, text="Sort by Song Album", command=sort_song_album)

    # Add the buttons to the window
    button1.pack()
    button2.pack()
    button3.pack()

#EXAMPLE DATA
#music = [("Drake","God's plan","2018", 3.19),("ArtistB","SongB","2018", 3.19),("ArtistA","SongA","2015",2.54),("ArtistC","SongC","2017",3.24),("Future","Mask Off","2014",3.45)]
#EXAMPLE DATA

#Empty list for mp3s
music = []

def output_sorted_data(list,type):
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END) #wipes console
    for item in list:
        if type == 'title':
            output_text.insert(tk.END, str(item.title) + "\n")
        elif type == 'artist':
            output_text.insert(tk.END, str(item.artist) + "\n")
        elif type == 'album':
            output_text.insert(tk.END, str(item.album) + "\n")
    output_text.insert(tk.END, "Data sorted!\n")
    output_text.config(state=tk.DISABLED)

def sort_song_name():
    """A function that will sort songs by name when the sort button is clicked"""
    sorted_music = sorted(music, key = lambda x: x.title)
    output_sorted_data(sorted_music,'title')
    print("Sorting by song name...")
    # Close the window
    sort_window.destroy()

def sort_artist_name():
    """A function that will sort songs by artist when the sort button is clicked."""
    sorted_music = sorted(music, key = lambda x: x.artist)
    output_sorted_data(sorted_music,'artist')
    print("Sorting by artist name...")
    # Close the window
    sort_window.destroy()
    
def sort_song_album():
    """A function that will sort songs by album when the sort button is clicked."""
    sorted_music = sorted(music, key = lambda x: x.album)
    output_sorted_data(sorted_music,'album')
    print("Sorting by song album...")
    # Close the window
    sort_window.destroy()

# Upload file function
def upload_file():
    """A function that allows the user to upload .mp3 files into the program."""
    file_path = filedialog.askopenfilename()
    music.append(mp3.Mp3(file_path))
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END) #wipes console
    output_text.insert(tk.END, "Selected file:\n" + str(mp3.Mp3(file_path)) + "\n")
    output_text.config(state=tk.DISABLED)

# sync / refresh function
def sync_website():
    """A function to sync data."""
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Syncing Data...\n")
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

# sync button
ping_button_image = tk.PhotoImage(file="GUI_assets/sync.png")
ping_button = tk.Button(button_frame, image=ping_button_image, command=sync_website)
ping_button.pack(side=tk.LEFT)

# start
root.mainloop()