# import os
# basedir = r"C:\Users\Josep\Desktop\TestingPythonRenaming"
# os.chdir(basedir)
# for roots, dirs, files, in os.walk(basedir, topdown=False):
#     for dirs in dirs:
#         if "." in dirs:
#             city, date, = dirs.split('.')
#             new_name = date + " " + city
#             os.rename(dirs, new_name)



# from https://stackoverflow.com/questions/32380631/using-os-walk-in-python
import os
path = r"C:\Users\Josep\Desktop\TestingPythonRenaming"
for root, dirs, files in os.walk(path):  # parse through file list in the current directory
    for foldername in dirs:
        if "." in foldername:
            source_foldername = os.path.join(root, foldername)
            location, date, = foldername.split('.')
            new_name = (date + " " + location).title()
            print(new_name)
            target_foldername = os.path.join(root, new_name.replace(".", " "))  # convert .s to spaces
            os.rename(source_foldername, target_foldername)  # rename the file



# new_directory = r"D:\External Hard Drive Videos\MOOCs"
# for roots, dirs, files, in os.walk(new_directory):
#     if "python" in dirs:
#         print(dirs)


# import os
# for root, dirs, files in os.walk(r"C:\Users\Josep\Desktop\Coursera - Finance For Non Finance Managers", topdown=True):
#     for name in files:
#         file_name, file_ext = (os.path.splitext(name))
#         new_name = "{} - Bananas{}".format(file_name, file_ext)
#         os.rename(name, new_name)
#         print(name)
#


# import os
# basedir = r"C:\Users\Josep\Desktop\TestingPythonRenaming"
# for root, dirs, files in os.walk(basedir):
#     for filename in dirs:
#         location, date = filename.split(".")
#         os.rename(filename, date + " " + location)

