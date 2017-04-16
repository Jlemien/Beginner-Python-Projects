import os
path=r"C:\Users\Vericant\Documents\Subtitle QR 2016-2017"
for(path,dirs,files)in os.walk(path):
    print("This is the current folder:", path)
    print("This folder contains these subfolders:", dirs)
    print("This folder contains these files:", files)
    print("*****")