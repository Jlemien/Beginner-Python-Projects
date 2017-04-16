from tkinter import *

root = Tk()

def window(main):
    main.title('Joseph\'s Program')
    #root.geometry('350x300+450+200')
    main.update_idletasks()
    width = main.winfo_width()
    height = main.winfo_height()
    x = (main.winfo_screenwidth() // 2 ) - (width // 2 )
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def main_content():
    hello = Label(root, text='Hello from Joseph!', font='times 18 bold underline', fg='#42eef4', bg='#ffe500')
    hello.pack()
    second = Label(root, text='This is a test.', font='TkFixedFont 16')
    second.pack()
    left = Label(root, text='I\'m left', bg='red')
    left.pack(side=LEFT)
    bottom = Label(root, text='I\'m bottom', bg='blue')
    bottom.pack(side=BOTTOM)
    right = Label(root, text='I\'m right', bg='purple')
    right.pack(side=RIGHT)


window(root)
main_content()
mainloop()
