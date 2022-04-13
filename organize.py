import glob
from re import I
from tkinter import W
import os
from os import path

# Directory to Organize
directory = "/home/nickel/Downloads/"

# File Extensions
extensions = {}
extensions["Documents"] = [".pdf", ".docx", ".doc", ".csv"]
extensions["Pictures"] = [".jpeg", ".jpg", ".png", ".gif"]
extensions["Videos"] = [".mp4", ".avi", ".webm", ".mkv"]
extensions["Audio"] = [".mp3"]
extensions["Compressed"] = [".zip"]

# Count number of files moved for each extension
counter = {}

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
            if not path.exists(directory+str(key)):
                os.makedirs(directory + key)

            count = counter.get(key, 0) + 1  # update count 
            counter[key] = count
            print("-" + directory+str(key))

print("Finished organizing", directory, "directory.\nSummary: ")
total_count = 0
for key, value in counter.items():
    total_count += value
    print("- Moved ", str(value), " items to ", str(key))

print("Moved ", str(total_count), " files in total.")


