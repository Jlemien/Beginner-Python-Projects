import os

#You will have to make sure that the program is looking at the correct folder,
#which you can do with this:
os.chdir(r"C:\Users\Josep\Desktop\This Folder")
print(os.getcwd())

#Then you can use os.rename
previous_name = "ReNameMe.txt"
new_name = "ThisIsMyNewName.txt"
os.rename(previous_name, new_name)

#you can use the same method to move a file by modifying the new name
previous_name = "ReNameMe.txt"
new_name = "ampleFolder/ThisIsMyNewName.txt"
os.rename(previous_name, new_name)

#deleting a file is pretty easy:
os.remove(r"C:\Users\Josep\Desktop\Class 1 Finance For Non Finance Managers.mp4")