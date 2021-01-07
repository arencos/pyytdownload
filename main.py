import tkinter as tk
from tkinter import *
import pytube
from moviepy.editor import *
import os
import string
from tkinter import messagebox
import logging


logging.basicConfig(filename="log.txt", format='%(asctime)s - %(levelname)s - %(message)s')

valid_chars = "-_()üğçıİöÖÜĞÇI %s%s" % (string.ascii_letters, string.digits)
def download():
	try:
		url = E1.get()
		yt = pytube.YouTube(url)
		vid = yt.streams.get_highest_resolution()
		logging.info("Downloading video")
		print("Downloading video")
		vid.download()
		downloadedVideo = VideoFileClip(os.path.join(''.join(c for c in vid.title if c in valid_chars) + ".mp4"))
		downloadedVideo.audio.write_audiofile(os.path.join(''.join(c for c in vid.title if c in valid_chars) + ".mp3"))
		print("Done.")
	except Exception as e:
		messagebox.showerror("Error.", str(e))
		logging.error(str(e))
		print(str(e))

window = tk.Tk()
window.title("PyYtDownload")
aboutText = tk.Label(text = "PyYtDownload\nMade by https://github.com/arencos\nBuild:060121\nEnter link above to download files.\nOpen log from the button above\nNOTE: The app might freeze", foreground="yellow", background="black")

L1 = Label(window, text="URL")
E1 = Entry(window, bd = 5)
logInGui = tk.Text()

mp3Down = Button(window, text="Download (MP4 and MP3)", width=20, command=download)

T = tk.Text(window, height=10, width=40)
def redirector(inputStr):
    T.insert(tk.INSERT, inputStr)

sys.stdout.write = redirector

T.pack(side=tk.BOTTOM)
mp3Down.pack(side=tk.BOTTOM)
L1.pack(side=tk.BOTTOM)
E1.pack(side=tk.BOTTOM)
aboutText.pack()
window.mainloop()
