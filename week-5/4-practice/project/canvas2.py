from tkinter import *

master = Tk()

w = Canvas(master, width = 320, height = 320)
w.pack()

for n in range(64):
    offset = 20
    if n % 16 == 0 or n % 16 == 2 or n % 16 == 4 or n % 16 == 6 or n % 16 == 9 or n % 16 == 11 or n % 16 == 13 or n % 16 == 15:
        w.create_rectangle((n % 8) * offset, (n // 8) * offset, (n % 8) * offset + offset, (n // 8) * offset + offset, fill = "#000000")

mainloop()
