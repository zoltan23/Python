from tkinter import *

window = Tk()

filename = StringVar()
url = StringVar

def print_filename():
    url = e1.get()
    fileName = e2.get()
    print(url + "filename" + fileName)


e1 = Entry(window, textvariable = url)
e1.grid(row = 0, column = 1)

e2 = Entry(window, textvariable = url)
e2.grid(row = 1, column = 1)

t1 = Text(window, height=1, width=35)
t1.insert(END,"URL:")
t1.grid(row = 0, column = 0)

t2 = Text(window, height=1, width=35)
t2.insert(END,"Choose the name of the output file:")
t2.grid(row = 1, column = 0)

b1 = Button(window, text='Execute', command = print_filename)
b1.grid(row = 2)

print(url)


window.mainloop()


