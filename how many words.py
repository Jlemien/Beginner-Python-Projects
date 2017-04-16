import os
# -*- coding: utf-8 -*-
for root, dirs, files in os.walk("C:\\Users\\Josep\\Desktop\\How many words\\"):
    #    print(root)
    #    print(dirs)
    #    print(files)
    #    print("These are your files")

    for file in files:
        f = open(root +'\\'+ file)
        file_content = f.read()
        lines = file_content.split("\n")
        total_count = 0
        for line in lines:
            characters = line.split(" ")
            total_count += len(characters)
        #print(total_count)
# or I could use this if I want to know which file has how many words
        THISISTHEONE = '%s, %s' % (file, total_count)
        open("example.txt", 'r')

#How can I get this to write to a CSV file instead of simply printing the info into the shell?
#        
#        columns = '%s, %s' % (file, total_count))
#        write clums to EXCEL CSV
#
#        excel_file = r'C:\Users\Josep\Desktop\This folder\This spreadsheet.xlsx'
#        with open(excel_file, 'wb') as x_file:
#            x_file.write('{} TotalAmount'.format(data))
#
#text = "'%s, %s' % (file, total_count)"
#savefile = open('examplefile.txt','w')
#savefile.write(text)
#savefile.close
