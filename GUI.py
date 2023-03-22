import tkinter as tk
import mp3
from tkinter import ttk
from tkinter import filedialog

# Custom button class for hover effect
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.default_background = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.default_background

# Window creation
root = tk.Tk()
root.title("Pytunes")

# Set background color
root.configure(bg='#1a1a1a')

# Window size
root.geometry("675x450")

# Label for the output field
output_label = tk.Label(root, text="Output:", font=("Arial", 20), bg='#1a1a1a', fg='#ffffff')
output_label.pack(pady=10)

# Output field
output_text = tk.Text(root, font=("Arial", 14), height=12, wrap=tk.WORD, bg='#2b2b2b', fg='#ffffff')
output_text.config(state=tk.DISABLED)
output_text.pack(pady=10, padx=10)

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
    button4 = tk.Button(sort_window, text="Sort by Genre", command=sort_song_genre)

    # Add the buttons to the window
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

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
        elif type == 'genre':
            output_text.insert(tk.END, str(item.genre) + "\n")
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

def sort_song_genre():
    """A function that will sort songs by album when the sort button is clicked."""
    sorted_music = sorted(music, key = lambda x: x.genre)
    output_sorted_data(sorted_music,'genre')
    print("Sorting by song genre...")
    # Close the window
    sort_window.destroy()

# Upload file function
def upload_file():
    """A function that allows the user to upload .mp3 files into the program."""
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        music.append(mp3.Mp3(file_path))
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, "Selected file:\n" + str(mp3.Mp3(file_path)) + "\n")
    output_text.insert(tk.END, "All files selected.\n")
    output_text.config(state=tk.DISABLED)

# sync / refresh function
def sync_website():
    """A function to sync data."""
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Syncing Data...\n")
    output_text.config(state=tk.DISABLED)

# Frame for buttons
button_frame = tk.Frame(root, bg='#1a1a1a')
button_frame.pack(pady=10)

# upload file button
upload_button_image = tk.PhotoImage(file="GUI_assets/upload.png")
upload_button = HoverButton(button_frame, image=upload_button_image, command=upload_file, bg='#3b3b3b', activebackground='#4b4b4b')
upload_button.pack(side=tk.LEFT, padx=5)

# sort data menu button
sort_button_image = tk.PhotoImage(file="GUI_assets/sort.png")
sort_button = HoverButton(button_frame, image=sort_button_image, command=sort_data_menu, bg='#3b3b3b', activebackground='#4b4b4b')
sort_button.pack(side=tk.LEFT, padx=5)

# sync button
ping_button_image = tk.PhotoImage(file="GUI_assets/sync.png")
ping_button = HoverButton(button_frame, image=ping_button_image, command=sync_website, bg='#3b3b3b', activebackground='#4b4b4b')
ping_button.pack(side=tk.LEFT, padx=5)

# start
root.mainloop()