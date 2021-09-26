from tkinter import *
import random

canvas_width = 540
canvas_height = 960
is_game_over = False
score = 0
level = 0
RATE = 20
SPEED = 3
GRAVITY = 0.5
up_count = 0
PIPE_HOLE_HEIGHT = 250

tk = Tk()
tk.title("Flappy Bird")

tk.geometry("%dx%d" % (canvas_width, canvas_height))

w = Canvas(tk, width=canvas_width, height=canvas_height, bg="#4EC0CA", highlightthicknes=0)
w.pack()

# tạo ra 2 ống nước trên và dưới
pipe_up = w.create_rectangle(canvas_width - 100, 0, canvas_width, 300, fill="#75C12F", outline="#75C12F")
pipe_down = w.create_rectangle(canvas_width - 100, 300 + PIPE_HOLE_HEIGHT, canvas_width, canvas_height, fill="#75C12F",
                               outline="#75C12F")

txt_score = w.create_text(20, 45, text="0", fill="white", anchor=W, font="Impact 50")
txt_level = w.create_text(400, 60, fill="white", font="Impact 60", text="Lv. " + str(level), anchor=W)

bird_img = PhotoImage(file="D:\Study\Code\Python\Exercise\BT_PTUD_Mobile_python\PhatTrienUngDungMobile\FlappyBird2"
                           "/bird.png")
bird = w.create_image(75, canvas_height // 2, image=bird_img)

game_over_backgroud = txt_final_score = None


def restart_game():
    global SPEED, is_game_over, txt_final_score, game_over_backgroud, score, level
    score = 0
    w.itemconfig(txt_score, text="0")
    level = 0
    w.itemconfig(txt_level, text="Lv. 0")
    w.coords(bird, 75, canvas_height // 2)
    SPEED = 3
    x1 = canvas_width - 100
    y2 = random.randint(100, canvas_height - PIPE_HOLE_HEIGHT - 100)
    w.coords(pipe_up, x1, 0, x1 + 100, 350)
    w.coords(pipe_down, x1, y2 + PIPE_HOLE_HEIGHT, x1 + 100, canvas_height)
    if txt_final_score:
        w.delete(txt_final_score)
    if game_over_backgroud:
        w.delete(game_over_backgroud)
    is_game_over = True


def game_over():
    global score, is_game_over, game_over_backgroud, txt_final_score
    game_over_backgroud = w.create_rectangle(0, 0, canvas_width, canvas_height, fill="#4ec0ca", outline="#4ec0ca")
    txt_final_score = w.create_text(20, 45, text="Your score: %s" % score, fill="white", anchor=W, font="Impact 50")
    is_game_over = False


# làm cho chim chuyển động, rơi tự do theo chiều trọng lực, khi ấn space thì chim bay lên, thả thì nó rơi tự do
def bird_down():
    global SPEED, GRAVITY, RATE, is_game_over

    if is_game_over:
        x, y = w.coords(bird)
        y += SPEED
        SPEED += GRAVITY
        w.coords(bird, x, y)
        if (y > canvas_height):
            game_over()

    tk.after(RATE, bird_down)


def bird_up(evt=None):
    global SPEED, GRAVITY, RATE, up_count, is_game_over

    if is_game_over:
        x, y = w.coords(bird)
        SPEED = 4
        y -= 30 - up_count * 5
        if (up_count < 5):
            up_count += 1
            tk.after(RATE, bird_up)
        else:
            up_count = 0
        w.coords(bird, x, y)
    else:
        restart_game()


def pipe_move():
    global PIPE_HOLE_HEIGHT, score, is_game_over, level, RATE

    if is_game_over:
        x1, y1, x2, y2 = w.coords(pipe_up)
        xb, yb = w.coords(bird)
        x1 -= 5
        if (x1 < -100):
            x1 = canvas_width
            y2 = random.randint(75, canvas_height - PIPE_HOLE_HEIGHT - 75)
            score += 1
            w.itemconfig(txt_score, text=str(score))
            if score != 0 and score % 10 == 0:
                level += 1
            w.itemconfig(txt_level, text="Lv. " + str(level))

        w.coords(pipe_up, x1, 0, x1 + 100, y2)
        w.coords(pipe_down, x1, y2 + PIPE_HOLE_HEIGHT, x1 + 100, canvas_height)
        if xb + 90 > x1 and xb < x2 and (yb < y2 or yb + 64 > y2 + PIPE_HOLE_HEIGHT):
            game_over()
    tk.after(RATE, pipe_move)


tk.after(RATE, bird_down)  # sau 20ms thì chim bắt đầu rơi xuống
tk.after(RATE, pipe_move)

# lập trình mỗi khi nhấn phím cách thì chim bay lên
tk.bind("<space>", bird_up)
tk.bind("<Return>", bird_up)
tk.bind("<Button-1>", bird_up)  # khi nhấn trái chuột
tk.mainloop()
