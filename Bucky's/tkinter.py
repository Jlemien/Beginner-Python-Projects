from tkinter import *

root = Tk()

photo = PhotoImage(file="acupuncture.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()







"""
canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

canvas.delete(redLine)
canvas.delete(ALL)
"""


"""
import tkinter.messagebox
tkinter.messagebox.showinfo('Window Title', "Monkeys can live up to 300 years")

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print('  8==D~  ')
"""



"""
def doNothing():
    print("ok ok I won't...")

root = Tk()

# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label= "File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New ...", command=doNothing)
#subMenu.add_seperator()
subMenu.add_command(label="Exit", command=doNothing)
editMenu = Menu(menu)
menu.add_cascade()
menu.add_cascade(label= "Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# **** Toolbar ****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP)

root.mainloop()

# **** Status Bar ****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
"""



"""
class BuckysButtons:

 
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")

b = BuckysButtons(root)
"""

"""
def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()
"""

"""
def printName():
    print("Hello, my name is Bucky!")

button_1 = Button(root, text="Print my name.", command=printName)
button_1.pack()
"""


"""
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)
"""


"""
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Two", bg="blue", fg="yellow")
three.pack(side=LEFT, fill=Y)
"""

"""
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
"""