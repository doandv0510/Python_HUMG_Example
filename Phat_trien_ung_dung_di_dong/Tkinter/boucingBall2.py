from tkinter import *
import time

window = Tk()
window.title('bouncing ball')

dx = 5
dy = 5
game_over = 0

canvas = Canvas(window, width=640, height=480, bg='white')
canvas.pack()

ball = canvas.create_oval(10, 10, 30, 30, fill='red', outline='red')
rect = canvas.create_rectangle(250, 400, 400, 412, fill='blue', outline='blue')
text = canvas.create_text(320, 240, fill='red', font='Times 50 bold', text='Game Over!')
# oval = canvas.create_oval(10, 10, 150, 100, fill="blue")
# line = canvas.create_line(0, 150, 640, 150, fill="purple", width=5,dash=(4, 4, 2, 4))
#
# text = canvas.create_text(xc, yc, text="Hello", fill="blue", font=("Arial",20))

# def update_view
#     canvas.delete(oval)
#     for _ in range(25)
#         canvas.move(circle, 10, 0)
#         canvas.move(text, -10, 0)
#         time.sleep(0.04)
#         window.update()

# window.after(2000, update_view)

canvas.itemconfigure(text, state='hidden')


def move_left(evt):
    global game_over

    if game_over == 1:
        return
    c = canvas.coords(rect)
    if c[0] > 10:
        canvas.move(rect, -10, 0)


def move_right(evt):
    global game_over
    if game_over == 1:
        return
    c = canvas.coords(rect)
    if c[2] < 630:
        canvas.move(rect, 10, 0)


def restart(evt):
    global game_over

    canvas.coords(ball, 10, 10, 30, 30)
    canvas.coords(rect, 250, 400, 400, 412)
    canvas.itemconfigure(text, state='hidden')
    game_over = 0
    move_ball()


canvas.bind_all("<KeyPress-Left>", move_left)
canvas.bind_all("<KeyPress-Right>", move_right)
canvas.bind_all("<Button-1>", restart)


def move_ball():
    x1, y1, x2, y2 = canvas.coords(ball)
    xp1, yp1, xp2, yp2 = canvas.coords(rect)
    global dx
    global dy
    global game_over

    if y1 <= 0:
        dy = 5
    elif y2 >= 480:
        game_over = 1
        canvas.itemconfigure(text, state='normal')
    elif x1 <= 0:
        dx = 5
    elif x2 >= 640:
        dx = -5
    elif yp1 <= y2 <= yp2 and (xp1 <= x1 <= xp2 or xp1 <= x2 <= xp2):
        dy = -5

    canvas.move(ball, dx, dy)


if game_over == 0:
    window.after(30, move_ball)

while True:
    move_ball()
    window.update()
    time.sleep(0.03)

window.mainloop()