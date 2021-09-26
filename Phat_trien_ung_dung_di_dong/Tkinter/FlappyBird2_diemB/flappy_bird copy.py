#khai báo thư viện tkinter và random
from tkinter import *
import random

canvas_width = 540
canvas_height = 960
is_game_over = False
score = 0 # lưu điểm 
SPEED = 3 # tốc độ rơi
DELTA = 0.5 # gia tốc rơi
RATE = 20 # chu ki của chú chim// tốc độ của game
up_count = 0 # số lần bay lên 
PIPE_HOLE_HEIGHT = 250 # khoảng cách giữa 2 ống
level = 0 # lưu giá trị level

tk = Tk()
tk.title="Flappy Bird" 

#kích thước cửa sổ:
tk.geometry("%dx%d" % (canvas_width, canvas_height))

w = Canvas(tk, width=canvas_width, height= canvas_height, bg = "#4EC0CA", highlightthicknes=0) 
#sắp xếp w lên cửa sổ 
w.pack()

# tạo ra 2 ống nước trên và dưới
pipe_up = w.create_rectangle(canvas_width - 100, 0, canvas_width, 300, fill="#74BF2E", outline="#74BF2E")
pipe_down = w.create_rectangle(canvas_width - 100, 300 + PIPE_HOLE_HEIGHT, canvas_width, canvas_height, fill="#74BF2E", 
outline="#74BF2E")
# pipe_down = w.create_rectangle()

# hiển thị điểm của màn chơi
txt_score = w.create_text(20, 45, text="0", fill="white", anchor=W, font="Impact 50")
# hiển thị lv màn chơi
txt_level = w.create_text(400,60,fill="white",font="Impact 60",text="Lv. " + str(level), anchor=W)

#vẽ 1 con chim trên canvas   
bird_img = PhotoImage(file ="..\PhatTrienUngDungMobile\lappyBird2\bird.png") 
# tạo ra 1 cái image và tải ảnh trg file và gán vào biến
# đưa ảnh lên canvas với 2 tham số đầu tiên là x và y là vị trí đăt h.ảnh trên m.hình và đối tượng là h.ảnh mới tạo ra 
bird = w.create_image(75, canvas_height//2, image = bird_img)
# khởi tao lại game mới

game_over_backgroud = txt_final_score = None
def restart_game():
    global SPEED, is_game_over, txt_final_score, game_over_backgroud, score, level # khai báo biến bên ngoài hàm
    #set lại điểm chơi = 0
    score = 0
    w.itemconfig(txt_score, text="0")
    #set lại level game
    level = 0
    w.itemconfig(txt_level, text="Lv. 0")
    # trả lại vị trí ban đầu của chim
    w.coords(bird, 75, canvas_height//2)    
    #reset speed
    SPEED = 3
    # set lạ vị trí cột
    x1 = canvas_width - 100 # vị trí ngoài cùng bên phải
    y2 = random.randint(100, canvas_height - PIPE_HOLE_HEIGHT - 100)
    w.coords(pipe_up, x1, 0, x1+100, 350)
    w.coords(pipe_down, x1, y2 + PIPE_HOLE_HEIGHT, x1+100, canvas_height) 
        # y cua pipe_down luôn luôn bắt dầu từ y2 + pipe_hole_height và kết thúc luôn luôn bằng canvas_height
    # xóa bớt game_over_backgroud, txt_final_score đi 
    if txt_final_score:
        w.delete(txt_final_score)
    if game_over_backgroud:
        w.delete(game_over_backgroud)
    
    is_game_over = True

def game_over():
    global score, is_game_over, game_over_backgroud, txt_final_score
    game_over_backgroud = w.create_rectangle(0, 0, canvas_width, canvas_height, fill="#4ec0ca", outline="#4ec0ca")
    txt_final_score = w.create_text(20,45, text="Your score: %s" % score, fill="white", anchor = W, font="Impact 50")
    is_game_over = False


#làm cho chim chuyển động, rơi tự do theo chiều trọng lực, khi ấn space thì chim bay lên, thả thì nó rơi tự do
def bird_down():
    global SPEED, DELTA, RATE, is_game_over # khai báo biến bên ngoài hàm

    if is_game_over: # kiểm tra game có chạy hay ko 
        #canvas được đánh gốc tọa độ 0 0 ở góc trên bên trái , sang phải x tăng dần và y đi xg tăng dần
        # nên khi chim rơi xuống là y tăng lên
        # tìm tọa độ x,y hiện tại của chim
        x, y = w.coords(bird)

        # làm tốc độ chim hạ cánh tăng dần, tạo ra biến với tốc độ ban đầu của chim
        
        y+=SPEED # chim rơi xuống với tốc độ bằng speed
        SPEED += DELTA # tốc độ tăng lên với delta

        #gọi lại hàm coods với tham số là bird và truyền thêm tham số để thay dổi tọa độ chim
        w.coords(bird, x, y)
        #kiểm tra y chạm đáy màn hình
        if(y>canvas_height):
            game_over()
        #vì bird_down được gọi 1 lần sau 20ms với lệnh after, nên rơi xuống đúng 10 điểm ảnh là dừng lại luôn,
        # vây để nó cahyj tiếm ta gọi lại hàm hàm bird_dowm trong 20ms tiếp theo

    tk.after(RATE, bird_down)
    
def bird_up(evt=None):# đặt giá trị mặc định của evt = none
    global SPEED, DELTA, RATE, up_count, is_game_over
    
    if is_game_over: # kiểm tra game có chạy hay ko 
        # tương tự bird_down, ta lấy giá trị ban đầu của chim
        x, y = w.coords(bird)
        # đăt lại tốc độ rơi ban đầu chứ ko phải là tốc độ rơi tiếp theo sau khi nhấn nút
        SPEED = 4
        y -= 30 - up_count * 5 # nhảy lên từ từ cho chim
        # làm chim nhẩy lên 5 lần với mỗi lần = 30 điểm ảnh
        if(up_count < 5):
            up_count+=1
            tk.after(RATE, bird_up) # sau 1 khoản time = rate gọi lại bird_up
        else:
            up_count = 0 # rester lượt bấm

        #xét lại vị trí con chim
        w.coords(bird, x, y)
    else:
        restart_game()

def pipe_move():
    global PIPE_HOLE_HEIGHT, score, is_game_over, level, RATE

    if is_game_over: # kiểm tra game có chạy hay ko 
        x1, y1, x2, y2 = w.coords(pipe_up) # tọa độ 4 góc cảu ống ban đầu
        xb, yb = w.coords(bird) # lấy lại giá trị tọa độ của chim
        # do x đi từ phải qua trái nên x giảm dần
        x1 -= 5
        # kiểm tra nếu ống ra khỏi màn hinh thì tạo lại 1 ống khác tạo ra
        if(x1 <-100):
            x1 = canvas_width
            # random vị trí xuất hiện lỗ hổng giữa 2 ống
            y2 = random.randint(75, canvas_height - PIPE_HOLE_HEIGHT - 75 )
             # random từ 75 - > ... để tránh lỗ chạm 2 cạnh trên và dưới màn hình
            score += 1
            w.itemconfig(txt_score, text=str(score))
            if score != 0 and score % 10 == 0:
                level += 1
            w.itemconfig(txt_level, text="Lv. "+str(level))
            # cập nhật lại txt_score sau mỗi lần tăng điểm
            
        w.coords(pipe_up, x1, 0, x1+100, y2)
        w.coords(pipe_down, x1, y2 + PIPE_HOLE_HEIGHT, x1+100, canvas_height) 
        # y cua pipe_down luôn luôn bắt dầu từ y2 + pipe_hole_height và kết thúc luôn luôn bằng canvas_height
        if xb+90 > x1 and xb < x2 and (yb < y2 or yb + 64 > y2 + PIPE_HOLE_HEIGHT):
            game_over()
    tk.after(RATE, pipe_move)
        

tk.after(RATE, bird_down)# sau 20ms thì chim bắt đầu rơi xuống
tk.after(RATE, pipe_move) # tương tự hàm di chuyển chim,cũng sau 20ms thì di chuyển ống từ phải qua trái

# lập trình mỗi khi nhấn phím cách thì chim bay lên
tk.bind("<space>", bird_up)
tk.bind("<Return>", bird_up)
tk.bind("<Button-1>", bird_up) # khi nhấn trái chuột
tk.mainloop()