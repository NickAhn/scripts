import glob
from tkinter import W
import os
from os import path

# Directory to Organize
directory = "/home/nickel/Downloads/"

#File Extensions
extensions = {}
extensions["documents"] = [".pdf", ".docx", ".doc", ".csv"]
extensions["pictures"] = [".jpeg", ".jpg", ".png", ".gif"]
extensions["videos"] = [".mp4", ".avi", ".webm", ".mkv"]
extensions["audio"] = [".mp3"]
extensions["compressed"] = [".zip"]

'''
for file in DownloadsFolder:
    for type, extension in extensions:
        if file is in extension (list)
            move to /home/nickel/type
'''

# For all files in directory, check which extension it has and move to appropriate folder.
for file in glob.glob(directory + "*"):
    for key in extensions.keys():
        if os.path.splitext(file)[1] in extensions[key]:
            if path.exists(directory+str(key)):
                print("-" + directory+str(key))

