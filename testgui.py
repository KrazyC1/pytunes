from tkinter import *
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

#Client ID
ci = "cb6906d5bc1c4f80bbeb8006ec63bf42"

#Client Secret
cs = "42f643e0fb444dc1845f08cddc234908"

#Client Id and Secret Id have been embedded to the file so that we can hopelly all work with the API
client_credentials_manager = SpotifyClientCredentials(client_id=ci, client_secret=cs) #check definition to change API connection
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

root = Tk()
root.geometry("450x450")
root.title(" Spotify Search ")

def Take_input():
	Output.delete("1.0","end")
	INPUT = inputtxt.get("1.0", "end-1c")
	print("Searching for: " + INPUT)
	results = sp.search(q=INPUT, limit=20)
	for i, t in enumerate(results['tracks']['items']):
		Output.insert(END, f"{i+1}. {t['name']}\n")
	
l = Label(text = "What would you like to search? ")
inputtxt = Text(root, height = 2,
				width = 50,
				bg = "light yellow")

Output = Text(root, height = 20,
			width = 50,
			bg = "light cyan")

Display = Button(root, height = 2,
				width = 20,
				text ="Search",
				command = lambda:Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
