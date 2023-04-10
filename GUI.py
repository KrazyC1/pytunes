import tkinter as tk
import mp3
from tkinter import ttk
from tkinter import filedialog
import spotify

# Global variable to store the order of sorting
ascending_order = True
sorting_column = 'title'

#Refrencing spotify.py
s = spotify.Spotify()

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
root.minsize(675, 550)

# Load the image for the output label
output_image = tk.PhotoImage(file="GUI_assets/Pytunes_banner.png")

# Label for the output field
output_label = tk.Label(root, image=output_image, bg='#1a1a1a')
output_label.pack(pady=10)

# Search button
def search_music():
    """A function to search for music."""
    search_term = search_entry.get()
    if search_term:
        matching_music = [item for item in music if search_term.lower() in item.title.lower() or search_term.lower() in item.artist.lower() or search_term.lower() in item.album.lower() or search_term.lower() in item.genre.lower()]
        output_sorted_data(matching_music,'title')
    else:
        print("Please enter a search term.")

# Search bar frame
search_bar_frame = tk.Frame(root, bg='#1a1a1a')
search_bar_frame.pack(pady=10)

# Home button function
def display_all_songs():
    output_sorted_data(music, 'title')
    search_entry.delete(0, tk.END)

# Home button
home_button_image = tk.PhotoImage(file="GUI_assets/home.png")
home_button = HoverButton(search_bar_frame, image=home_button_image, command=display_all_songs, bg='#3b3b3b', activebackground='#4b4b4b')
home_button.pack(side=tk.LEFT, padx=5, pady=5)

# Search bar entry
style = ttk.Style()
style.configure("TEntry", fieldbackground='#2b2b2b', background='#2b2b2b', foreground='#000000', bordercolor='#2b2b2b', lightcolor='#2b2b2b', darkcolor='#2b2b2b', borderwidth=20, relief=tk.GROOVE)
search_entry = ttk.Entry(search_bar_frame, width=30, font=("Arial", 14), style='TEntry')
search_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Search button
search_button_image = tk.PhotoImage(file="GUI_assets/search.png")
search_button = HoverButton(search_bar_frame, image=search_button_image, command=search_music, bg='#3b3b3b', activebackground='#4b4b4b')
search_button.pack(side=tk.LEFT, padx=5, pady=5)

# Switch button function
def switch_function():
    global ascending_order
    ascending_order = not ascending_order
    output_sorted_data(music, sorting_column, reverse=not ascending_order)

switch_button_image = tk.PhotoImage(file="GUI_assets/switch.png")
switch_button = HoverButton(search_bar_frame, image=switch_button_image, command=switch_function, bg='#3b3b3b', activebackground='#4b4b4b')
switch_button.pack(side=tk.RIGHT, padx=5, pady=5)
switch_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Center the search bar
search_bar_frame.pack(anchor='center')

# Output field - Replacing the Text widget with a Treeview widget
columns = ("Title", "Artist", "Album", "Genre", "Length")
output_tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    output_tree.heading(col, text=col)
output_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

output_tree.column("Title", width=100, minwidth=100, anchor=tk.CENTER)
output_tree.column("Artist", width=100, minwidth=100, anchor=tk.CENTER)
output_tree.column("Album", width=100, minwidth=100, anchor=tk.CENTER)
output_tree.column("Genre", width=100, minwidth=100, anchor=tk.CENTER)
output_tree.column("Length", width=100, minwidth=100, anchor=tk.CENTER)

def sort_data_menu():
    """A function for the sort data menu."""
    global sort_window
    sort_window = tk.Toplevel()
    sort_window.resizable(False, False)

    # Create a gradient background using rectangles
    canvas = tk.Canvas(sort_window, width=200, height=200)
    red_start, green_start, blue_start = 70, 0, 192
    red_end, green_end, blue_end = 190, 0, 255

    for i in range(200):
        red = red_start + int((red_end - red_start) * i / 200)
        green = green_start + int((green_end - green_start) * i / 200)
        blue = blue_start + int((blue_end - blue_start) * i / 200)
        color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
        canvas.create_rectangle(i, 0, i + 1, 200, outline=color, fill=color)

    # Create the buttons
    button1 = tk.Button(sort_window, text="Sort by Song Name", command=sort_song_name)
    button2 = tk.Button(sort_window, text="Sort by Artist Name", command=sort_artist_name)
    button3 = tk.Button(sort_window, text="Sort by Song Album", command=sort_song_album)
    button4 = tk.Button(sort_window, text="Sort by Genre Type", command=sort_song_genre)
    button5 = tk.Button(sort_window, text="Sort by Song Length", command=sort_song_length)

    # Add the buttons to the canvas
    canvas.create_window(100, 20, window=button1)
    canvas.create_window(100, 60, window=button2)
    canvas.create_window(100, 100, window=button3)
    canvas.create_window(100, 140, window=button4)
    canvas.create_window(100, 180, window=button5)

    # Pack the canvas
    canvas.pack()

#EXAMPLE DATA
#music = [("Drake","God's plan","2018", 3.19),("ArtistB","SongB","2018", 3.19),("ArtistA","SongA","2015",2.54),("ArtistC","SongC","2017",3.24),("Future","Mask Off","2014",3.45)]
#EXAMPLE DATA

#Empty list for mp3s
music = []

def output_sorted_data(list, type, reverse=False):
    global sorting_column
    sorting_column = type
    output_tree.delete(*output_tree.get_children())  # Clears existing rows
    sorted_list = sorted(list, key=lambda x: getattr(x, type), reverse=reverse)
    
    for item in sorted_list:
        # Convert length to minutes:seconds format
        minutes, seconds = divmod(item.length, 60)
        duration = f"{int(minutes)}:{int(seconds):02d}"
        output_tree.insert("", tk.END, values=(item.title, item.artist, item.album, item.genre, duration))

def sort_song_length():
    """A function that will sort songs by length when the sort button is clicked."""
    sorted_music = sorted(music, key=lambda x: x.length)
    output_sorted_data(sorted_music, 'length')
    print("Sorting by song length...")
    # Close the window
    sort_window.destroy()

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
        output_sorted_data(music, 'title')

def sync_website():
    """A function to sync data."""
    for song in music:
        s.sync_spotify(song)
    print("Syncing Data...")

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