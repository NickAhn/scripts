import glob
from re import I
from tkinter import W
import os
from os import path
import shutil
from venv import create

# Directory to Organize
directory = "/home/nickel/Downloads/"

# File Extensions
extensions = {}
extensions["Documents"] = [".pdf", ".docx", ".doc", ".csv", ".pptx"]
extensions["Pictures"] = [".jpeg", ".jpg", ".png", ".gif", ".JPG", ".PNG", ".HEIC"]
extensions["Videos"] = [".mp4", ".avi", ".webm", ".mkv"]
extensions["Audio"] = [".mp3"]
extensions["Compressed"] = [".zip"]

# Count number of files moved for each folder 
counter = {}

def makedir(folder_path):
    if not path.exists(folder_path):
        os.makedirs(folder_path)

# Try to move file. If Duplicate is found, ask user if the file being moved should be deleted.
def move_file(file, path):
    try:
        shutil.move(file, path)
        count = counter.get(key, 0) + 1  # update count 
        counter[key] = count
    except shutil.Error:
        print("\n - Found duplicate of: ", file)
        response = input("   Remove file? (Y/n) ")
        if response.lower() == 'y':
            os.remove(file)
            print("   Removed ", file)
        pass


# Make Directories for each extension
for key in extensions.keys():
    makedir(directory + key)
makedir(directory + "Other")

# For all files in directory, check which extension it has and move to appropriate folder.
for file in glob.glob(directory + "*"):
    #ignore directories
    if file.find(".", 1) == -1: 
        continue

    moved_file = False
    for key in extensions.keys():
        if os.path.splitext(file)[1] in extensions[key]:
            # shutil.move(file, directory+key)
            move_file(file, directory+key)
            moved_file = True
            break

    if moved_file == True:
        continue

    count = counter.get("Other", 0) + 1  # update count 
    counter["Other"] = count
    shutil.move(file, directory+"Other")


print("\nFinished organizing", directory, "directory.\nSummary: ")
total_count = 0
for key, value in counter.items():
    total_count += value
    print("- Moved ", str(value), " items to ", str(key))

print("Moved ", str(total_count), " files in total.")


