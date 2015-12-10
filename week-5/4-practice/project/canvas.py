from tkinter import *

master = Tk()

w = Canvas(master, width = 320, height = 320)
w.pack()

lines = [0, 1, 2, 3, 4, 5, 6, 7]

for line in lines:
    if line % 2 == 1:
        number_of_black_squares_in_line_A = 4
        x = 0
        y = line * 20
        i = 20
        j = line * 20 + 20
        while number_of_black_squares_in_line_A > 0:
            w.create_rectangle(x, y, i, j, fill = "#000000")
            x += 40
            i += 40
            number_of_black_squares_in_line_A -= 1
    else:
        number_of_black_squares_in_line_B = 4
        x = 20
        y = line * 20
        i = 40
        j = line * 20 + 20
        while number_of_black_squares_in_line_B > 0:
            w.create_rectangle(x, y, i, j, fill = "#000000")
            x += 40
            i += 40
            number_of_black_squares_in_line_B -= 1

mainloop()
