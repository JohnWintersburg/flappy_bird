import tkinter
import random
import threading
window = tkinter.Tk()
window.title("Flappy bird")
window.geometry("500x500")
canvas = tkinter.Canvas(window, width=400, height=450, bg='white')
canvas.pack()
global first_right_col_x
first_right_col_x = 380
global second_right_col_x
second_right_col_x = 580
firsty = random.randint(80,420)
firsty1 = firsty-120
secondy = random.randint(80,420)
secondy1 = secondy-120
a = canvas.create_line(300, 450, 300, firsty)
b = canvas.create_line(first_right_col_x, 450, first_right_col_x, firsty)
c = canvas.create_line(300, firsty, 380, firsty) 
d = canvas.create_line(300, firsty1, 300, 0)
e = canvas.create_line(380, firsty1, 380, 0)
f = canvas.create_line(300, firsty1, 380, firsty1)

g = canvas.create_line(500, 450, 500, secondy)
h = canvas.create_line(second_right_col_x, 450, second_right_col_x, secondy)
i = canvas.create_line(500, secondy, 580, secondy)
j = canvas.create_line(500, secondy1, 500, 0)
k = canvas.create_line(580, secondy1, 580, 0)
l = canvas.create_line(500, secondy1, 580, secondy1)

bird = canvas.create_rectangle(15, 0, 30, 30, fill="#020202")
def play():
    threading.Timer(0.01, play).start()
    canvas.move(a, -1, 0)
    global first_right_col_x
    first_right_col_x -= 1
    global second_right_col_x
    second_right_col_x -= 1
    canvas.move(b, -1, 0)
    canvas.move(c, -1, 0)
    canvas.move(d, -1, 0)
    canvas.move(e, -1, 0)
    canvas.move(f, -1, 0)
    canvas.move(g, -1, 0)
    canvas.move(h, -1, 0)
    canvas.move(i, -1, 0)
    canvas.move(j, -1, 0)
    canvas.move(k, -1, 0)
    canvas.move(l, -1, 0)
    canvas.move(bird, 0, +2)
    if first_right_col_x == 0:
        first_right_col_x = 500
        firsty = random.randint(150,420)
        firsty1 = firsty-120
        canvas.coords(a, 420, firsty, 420, 450)
        canvas.coords(b, first_right_col_x, 450, first_right_col_x, firsty)
        canvas.coords(c, 420, firsty, 500, firsty)
        canvas.coords(d, 420, firsty1, 420, 0)
        canvas.coords(e, 500, firsty1, 500, 0)
        canvas.coords(f, 420, firsty1, 500, firsty1)
    if second_right_col_x == 0:
        second_right_col_x = 500
        secondy = random.randint(150,420)
        secondy1 = secondy-120
        canvas.coords(g, 420, secondy, 420, 450)
        canvas.coords(h, second_right_col_x, 450, second_right_col_x, secondy)
        canvas.coords(i, 420, secondy, 500, secondy)
        canvas.coords(j, 420, secondy1, 420, 0)
        canvas.coords(k, 500, secondy1, 500, 0)
        canvas.coords(l, 420, secondy1, 500, secondy1)
def fly():
    canvas.move(bird, 0, -60)
btn = tkinter.Button(window, text="Play", command = play)
flying = tkinter.Button(window, text="fly", command = fly)
btn.pack()
flying.pack()
window.mainloop()
change()