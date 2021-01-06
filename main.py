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
		logging.debug("Downloading video")
		vid.download()
		downloadedVideo = VideoFileClip(os.path.join(''.join(c for c in vid.title if c in valid_chars) + ".mp4"))
		downloadedVideo.audio.write_audiofile(os.path.join(''.join(c for c in vid.title if c in valid_chars) + ".mp3"))
	except Exception as e:
		messagebox.showerror("Error.", "An error occured in the function download(). This means either the video is private, you entered the link wrong or another error. Check the link you entered. Here is the error message in case it was not because of the things above. " + str(e))
		logging.error(str(e))



window = tk.Tk()
window.title("PyYtDownload")
aboutText = tk.Label(text = "PyYtDownload\nMade by https://github.com/arencos\nBuild:060121\nEnter link above to download files.\nNOTE: The app might freeze", foreground="yellow", background="black")

L1 = Label(window, text="URL")
E1 = Entry(window, bd = 5)

mp3Down = Button(window, text="Download (MP4 and MP3)", width=20, command=download)

L1.pack()
E1.pack()
mp3Down.pack()
aboutText.pack()
window.mainloop()