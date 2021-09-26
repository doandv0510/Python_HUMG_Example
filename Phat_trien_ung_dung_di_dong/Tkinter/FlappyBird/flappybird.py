from tkinter import *
# thư viện
import random
import  time
is_game_over = False
# để mình vô còn chơi nếu bằng true thì game over
end_game_bg = None
# Không hiện thị bg end game cho đến khi kết thúc
end_game_score = None
# Không hiện thị điểm cho đến khi kết thúc
ms = 20
score = 0
level = 1
plus = 1
window = Tk()
# window là 1 biến cả chương trình dùng biến này để chạy thư viện tkinter
window.title('Flappy bird')
# đặt tên cửa sổ là flappy bird
cw, ch = 540, 960
# cw là chiều rộng của cửa sổ anvas khi chạy chương trình
# ch là chiều dài của cửa sổ canvas khi chạy chương trình
canvas = Canvas(window, width = cw, height = ch, bg = '#43f0bf', highlightthickness = 0)
canvas.pack()
d = 200
pipeup= canvas.create_rectangle(cw - 100, 0, cw, 350, fill = '#3734eb', outline = '#3734eb')
# vẽ ống cống ở trên
pipedown = canvas.create_rectangle(cw - 100, 600, cw, ch, fill = '#3734eb', outline = '#3734eb')
# vẽ ống cống ở dưỡi
text = canvas.create_text(15,60,fill="white",font="Impact 60",text=str(score), anchor=W)
# tạo dòng text để in ra số điểm chúng ta được
lv_text = canvas.create_text(400,60,fill="white",font="Impact 60",text="Lv. " + str(level), anchor=W)
# in ra level đạt đụowc
bird_img = PhotoImage(file ='PhatTrienUngDungMobile/FlappyBird/bird3.png')
# lấy ảnh con chim trong thư mục đấy
bird = canvas.create_image(100, ch // 2, image = bird_img)
# xét kích thước cho con chim


gravity = 0
# tốc độ rơi
acer = 0.5
# theo vật lý một vật càng rơi xuống càng nhanh 
def bird_fall():
    global gravity, acer, is_game_over
    # gravity là tốc độ rơi, acer là đơn vị + vào gravity
    # biến trong hàm tách biệt thì phải dùng global 
    if is_game_over:
        return
    # Nếu như game over rồi thì return thoát khỏi hàm luôn
    x1, y1 = canvas.coords(bird) 
    # x1, y1 chúng ta lấy tọa độ con bird
    y1 += gravity
    # lấy y1 += gravity là cho gravity xuống tiếp
    gravity += acer
    # gravity += acer là tăng tốc độ rơi lên
    if y1 > ch:
        game_over()
    # ở đây tức là nó đang ở dưới màn hình rồi thì gameover luôn
    canvas.coords(bird, x1, y1)
    # xét lại 2 biến tọa độ
    window.after(25, bird_fall)
    # lặp lại hàm bird_fall
    # đây là 20 mili s
up_count = 0
# hàm bird_up dùng để cho chim đi lên
def bird_up(evt=None):
    global up_count, gravity, is_game_over
    # up_count là để cho con chim bay lên
    if is_game_over:
        restart_game()
        return
    x1, y1 = canvas.coords(bird)
    # lấy tọa độ con chim
    gravity = 0
    # khi đi lên gravity dĩ nhiên để bằng 0
    y1 -= 25 - up_count * 5
    if up_count < 5:
        up_count += 1
        window.after(20, bird_up)
    else:
        up_count = 0
    canvas.coords(bird, x1, y1)
# move_pile di chuyển các ống cống
def move_pile():
    global  plus, is_game_over, score, ms, level
    # ms là mili s lập lại lúc level càng lên thì nó càng bé để chạy nhanh hơn
    if is_game_over:
        return
    x1, y1 , x2, y2 = canvas.coords(pipeup)
    # lấy tọa độ ống cống
    x1 -= 5
    # di chuyển sang bên trái bằng cách thay đổi x1
    if x1 < -100:
        x1 = cw
        y2 = random.randint(100, ch - 350)
        plus = 0
    # xét ống cốc trở lại và cho 1 ống cốc khác đi ra
    canvas.coords(pipeup, x1, 0, x1 + 100, y2)
    canvas.coords(pipedown, x1, y2 + 250, x1 + 100, ch)
    check_col()

    window.after(int(ms), move_pile)
    # hàm after không nhập vào số thực nên phải làm thế

def check_col():
    # hàm kiểm tra va chạm
    global score, plus, is_game_over, ms, level
    if is_game_over:
        return
    bird_w = 100
    # chiều dài con chim
    bird_h = 70
    # chiều rộng con chim
    x, y = canvas.coords(bird)
    # tạo độ chim
    xp, yp, xp2, yp2 = canvas.coords(pipeup)
    # tọa độ ống nước
    if x < xp2 and x + bird_w > xp + 50 and (y + bird_h > yp2 + 250 or y < yp2):
        # kiểm cha con chim có va chạm với ống cống hay không
        game_over()
    elif y > yp2:
        # đã qua ống cốc rồi 
        if plus == 0:
            # để phòng chống điểm nó + liên tục
            score += 1
            if score != 0 and score % 10 == 0:
                # tức là score là 10 20 gì đó thì level lên 1
                level += 1
                ms *= 0.9
                # điều chỉnh tốc độ
            plus = 1
            # không cộng nữa
            canvas.itemconfig(text, text=str(score))
            # xét lại điểm
            canvas.itemconfig(lv_text, text="Lv. " + str(level))
            # xét lại level

move_pile()
bird_fall()
def game_over():
    global is_game_over, end_game_bg, end_game_score
    is_game_over = True
    end_game_bg = canvas.create_rectangle(0, 0, cw, ch, fill = "#4EC0CA", outline = "white")
    end_game_score = canvas.create_text(15,200,fill="#ffffff",font="Impact 60",text="Your score is: " + str(score), anchor=W)
def restart_game():
    global is_game_over, end_game_bg, end_game_score, score, gravity, level, ms
    canvas.delete(end_game_bg)
    canvas.delete(end_game_score)
    score = 0
    canvas.itemconfig(text, text=str(score))
    level = 1
    canvas.itemconfig(lv_text, text="Lv. " + str(level))
    ms = 20
    canvas.coords(bird, 100, ch // 2)
    canvas.coords(pipeup, cw - 100, 0, cw, 350)
    canvas.coords(pipedown, cw - 100, 600, cw, ch)
    is_game_over = False
    gravity = 0
    move_pile()
    bird_fall()

window.bind('<space>', bird_up)
window.mainloop()
