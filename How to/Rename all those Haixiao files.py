# from https://stackoverflow.com/questions/32380631/using-os-walk-in-python
import os
path = r"C:\Users\Josep\Desktop\TestingPythonRenaming"
for root, dirs, files in os.walk(path):  # parse through file list in the current directory
    for foldername in dirs:
        if "." in foldername: #if the folder is names in the ugly way with a period
            source_foldername = os.path.join(root, foldername)
            location, date, = foldername.split('.')
            new_name = (date + " " + location).title() #make the name nicer to view, with date first and the location second
            print(new_name)
            target_foldername = os.path.join(root, new_name.replace(".", " "))  # convert the period to spaces
            os.rename(source_foldername, target_foldername)  # rename the file
