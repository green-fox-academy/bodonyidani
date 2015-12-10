from tkinter import *

master = Tk()

w = Canvas(master, width = 600, height = 600)
w.pack()

for n in range (600):
    offset = 6
    if n % 6 == 0:
        w.create_line(n + offset, 0, 600, n + offset, fill = "#dd0000")
    elif n % 6 == 3:
        w.create_line(n + offset, 0, 600, n + offset, fill = "#dddddd")

mainloop()
