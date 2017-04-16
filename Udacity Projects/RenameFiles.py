import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Josep\Videos\MOOCs\Coursera - Corporate Finance")
    print(file_list)    
    os.chdir(r"C:\Users\Josep\Videos\MOOCs\Coursera - Corporate Finance")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "index "))       
rename_files()