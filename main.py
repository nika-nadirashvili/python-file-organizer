# Python File Organizer 
# This program scans a folder and displays its files
import os
def show_files(folder):
    files = os.listdir(folder)
    print("Files found:")
    for file in files:
        print(file)
folder_path = input("Enter folder path: ")
show_files(folder_path)
