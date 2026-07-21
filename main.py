import os

folder = input("Enter folder path: ")

files = os.listdir(folder)

print("Files found:")

for file in files:
    print(file)
