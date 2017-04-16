# text = "Sample text to save \n This is a new line!!!"
# savefile = open('examplefile.xlsx','w')
# savefile.write(text)
# savefile.close


# filename = "example_file.txt"
# file = open(filename, 'w')
# for i in range(0,11):
#     file.write("This is line %i.\n" % i)
#
# file = open(filename, 'r')
# for line in file:
#     print(line, end = '')
# file.close()


filename = "example_file.txt"

file = open(filename, 'a')

for i in range(0,5):
    name = input("Enter a name: ")
    file.write(name + "\n")

file.close()
