"""
This code is from the StackOverflow question "Issue with renaming a bunch of files in a directory using Python"
(https://stackoverflow.com/questions/28270451/issue-with-renaming-a-bunch-of-files-in-a-directory-using-python)

It was offered as an alternative to the Udacity assignment for renaming files.
"""

import os
import re

def rename_files():
    file_list = os.listdir(r"C:\Users\Josep\Videos\MOOCs\Coursera - Corporate Finance")
    print(file_list)
    saved_path =os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"C:\Users\Josep\Videos\MOOCs\Coursera - Corporate Finance")
    for file_name in file_list:
        os.rename(file_name,re.sub("[a-z]","", file_name))
        os.chdir(saved_path)
rename_files()	