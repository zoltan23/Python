from tkinter import *
from roster_scraper import scrapeRoster
from tkinter import font as tkFont

window = Tk()

helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)

filename = StringVar()
url = StringVar

def print_filename():
    url = e1.get()
    scrapeRoster(url)

def clear():
    url = None

title = Text(window, height=1, width=35, font = helv36)
title.insert(END, "Scrape the Web!!!")
title.grid(row = 0, column = 0)

e1 = Entry(window, textvariable = url)
e1.grid(row = 1, column = 1)

e2 = Entry(window, textvariable = url)
e2.grid(row = 2, column = 1)

t1 = Text(window, height=1, width=35)
t1.insert(END,"URL:")
t1.grid(row = 1, column = 0)

t2 = Text(window, height=1, width=35)
t2.insert(END,"Choose the name of the output file:")
t2.grid(row = 2, column = 0)

b1 = Button(window, text='Execute', command = print_filename)
b1.grid(row = 3, column = 1)

b2 = Button(window, text='Clear', command = None )
b2.grid(row = 3, column = 2)

window.mainloop()


