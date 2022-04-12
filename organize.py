import glob
from tkinter import W
import os
from os import path


path = "/home/nickel/Downloads/*"
downloads_folder = glob.glob(path)

#Extensions
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

for file in downloads_folder:
    # print(os.path.splitext(file)[1])
    for key in extensions.keys():
        if os.path.splitext(file)[1] in extensions[key]:
            print(file) 
            #move file to path/key

