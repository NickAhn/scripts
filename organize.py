import glob
from re import I
from tkinter import W
import os
from os import path
import shutil

# Directory to Organize
directory = "/home/nickel/Downloads/"

# File Extensions
extensions = {}
extensions["Documents"] = [".pdf", ".docx", ".doc", ".csv", ".pptx"]
extensions["Pictures"] = [".jpeg", ".jpg", ".png", ".gif", ".JPG", ".PNG", ".HEIC"]
extensions["Videos"] = [".mp4", ".avi", ".webm", ".mkv"]
extensions["Audio"] = [".mp3"]
extensions["Compressed"] = [".zip"]

# Count number of files moved for each extension
counter = {}


# For all files in directory, check which extension it has and move to appropriate folder.
for file in glob.glob(directory + "*"):
    flag = False

    for key in extensions.keys():
        if os.path.splitext(file)[1] in extensions[key]:
            # create directory if it doesn't exist
            if not path.exists(directory+str(key)):
                os.makedirs(directory + key)

            shutil.move(file, directory+key)
            count = counter.get(key, 0) + 1  # update count 
            counter[key] = count
            flag = True
            break

    if flag == True:
        continue

    if not path.exists(directory+"Other"):
        os.makedirs(directory + "Other")

    count = counter.get("Other", 0) + 1  # update count 
    counter["Other"] = count
    shutil.move(file, directory+"Other")


print("\nFinished organizing", directory, "directory.\nSummary: ")
total_count = 0
for key, value in counter.items():
    total_count += value
    print("- Moved ", str(value), " items to ", str(key))

print("Moved ", str(total_count), " files in total.")


