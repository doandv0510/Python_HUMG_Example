import pygame # import thư viện
from random import randint
# khỏi tạo game bằng câu lệnh
pygame.init() #init là viết tắt của initialize: khởi tạo
  
screen = pygame.display.set_mode((400,670)) # tạo màn hình game với chiều ngang, cao 
pygame.display.set_caption('Flappy Bird'); # tiêu đề game
clock = pygame.time.Clock();
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
backGround_Img = pygame.image.load("PyGame/FlappyBird/Resource/images/backGround.png") # load ảnh nền, load vào đường đẫn url
backGround_Img = pygame.transform.scale(backGround_Img,(400,600)) # set tỉ lệ cho ảnh nền bằng cách gán lại biến . . .
#transform chuyển đổi, scale tỉ lệ( chỉnh lại tỉ lệ màn hình)
x_bird = 50
y_bird = 350
bird_Img = pygame.image.load('PyGame/FlappyBird/Resource/images/bird.png')
bird_Img = pygame.transform.scale(bird_Img,(45, 35)) # tọa tương tự với backgroud với tỉ lệ ảnh kahcs

scratch_Img = pygame.image.load('PyGame/FlappyBird/Resource/images/scratch.png')
scratch_Img = pygame.transform.scale(scratch_Img,(400,70))
# tọa ống
x_pipe1 = 300 # tọa độ x của các ống, tọa dộ y luôn bằng 0 nên ko cần khai báo
x_pipe2 = 500
x_pipe3 = 700
pipe_width = 50 # chiều rộng các ống bằng nhau
pipe1_height = randint(100,400) # chiều cao các ống chạy ngẫu nhiêu từ 100->400
pipe2_height = randint(100,400)
pipe3_height = randint(100,400)

pipe1_pass = False # kiểm tra dtg đi qua ống 1 hay chưa 
pipe2_pass = False
pipe3_pass = False

# vẽ ống
pipe_Img = pygame.image.load("PyGame/FlappyBird/Resource/images/tube.png")
pipe_op_Img = pygame.image.load("PyGame/FlappyBird/Resource/images/tube_op.png")
# khoảng cách giữa 2 ống
d_2pipe = 150
birdDropVelocity = 0 # tốc độ rơi của chú chim
gravity = 0.5
pipeMoveSpeed = 2

score = 0 # muốn tọa chữ t cần phải làm 3b: tạo font -> tạo chữ -> ghi chữ/ thể hiện lên màn hình
fontScore = pygame.font.SysFont('arial', 20)
fontGameOver = pygame.font.SysFont('arial', 30)
running = True  # biến trạng thái của trường chình
pausing = False # lưu trạng thái chạy của game (chay/ dừng)

#âm thanh
sound = pygame.mixer.Sound("PyGame/FlappyBird/Resource/no6.wav");

while running:
    clock.tick(60) # nháy 60 lần trg 1s, nếu ko có thì nháy theo tốc dộ max của máy tính
    screen.fill(WHITE) # đổ màu cho màn hình 
    backGround = screen.blit(backGround_Img,(0,0)) # vẽ ở tọa độ (0.0)
    pygame.mixer.Sound.play(sound) 
    # tạo ra các ống
    pipe1_img = pygame.transform.scale(pipe_Img,(pipe_width, pipe1_height)) #ép theo tỉ lệ width, height lấy ngẫu nhiên
    pipe1 =  screen.blit(pipe1_img,(x_pipe1, 0)) # vẽ ống mới tạo lên mà hình với tọa độ 
    
    pipe2_img = pygame.transform.scale(pipe_Img,(pipe_width, pipe2_height))
    pipe2 = screen.blit(pipe2_img, (x_pipe2, 0))

    pipe3_img = pygame.transform.scale(pipe_Img,(pipe_width, pipe3_height))
    pipe3 = screen.blit(pipe3_img, (x_pipe3, 0))

    
    # tạo ra các ống đối diện với ống phía trên
    pipe1_op_img = pygame.transform.scale(pipe_op_Img,(pipe_width, 600-(pipe1_height +  d_2pipe))) #ép theo tỉ lệ width, height = chiều cao màn hình - (chiều cao cột trên + k.c 2 cột)
    pipe1_op =  screen.blit(pipe1_op_img,(x_pipe1, pipe1_height +  d_2pipe)) # vẽ ống mới tạo lên mà hình với tọa độ x = tọa độ x cột trên 

    pipe2_op_img = pygame.transform.scale(pipe_op_Img,(pipe_width, 600-(pipe2_height +  d_2pipe))) 
    pipe2_op =  screen.blit(pipe2_op_img,(x_pipe2, pipe2_height +  d_2pipe)) 
    
    pipe3_op_img = pygame.transform.scale(pipe_op_Img,(pipe_width, 600-(pipe3_height +  d_2pipe)))
    pipe3_op =  screen.blit(pipe3_op_img,(x_pipe3, pipe3_height +  d_2pipe))
    #di chuyển các ống từ phải qua trái, x dảm dần nên ta trừ đi tốc độ di chuyển của ống
    x_pipe1 -= pipeMoveSpeed
    x_pipe2 -= pipeMoveSpeed
    x_pipe3 -= pipeMoveSpeed
    # tạo lại ống mới
    if(x_pipe1 < -pipe_width): # do chiều rộng của ống là 50 nên khi x của ống 1 = - độ rộng ống thì ống đó sẽ ra khỏi mang hinfg và ta tạo lại ống đó với chiều dài bằng 550
        x_pipe1 = 550
        pipe1_height = randint(100,400)
        pipe1_pass = False
    if(x_pipe2 < -pipe_width):
        x_pipe2 = 550
        pipe2_height = randint(100,400)
        pipe2_pass = False
    if(x_pipe3 < -pipe_width):
        x_pipe3 = 550
        pipe3_height = randint(100,400)
        pipe3_pass = False
    # vẽ chim
    bird = screen.blit(bird_Img,(x_bird, y_bird))
    #chim rơi. Do đối tg rơi từ trên xuống nên y của ta tăng dần
    y_bird = y_bird + birdDropVelocity
    birdDropVelocity += gravity
    
    # hiển thi điểm
    printScore = fontScore.render("Score: "+ str(score), True, BLACK) #font font chữ vừa tạo bên trên, render: vẽ score trên màn hình, tạo chữ
    screen.blit(printScore, (5,0)) # hiển thị điểm lên màn hình

    # ghi điểm
    if x_pipe1 + pipe_width < x_bird and pipe1_pass == False:
        score += 1
        pipe1_pass = True
    if x_pipe2 + pipe_width < x_bird and pipe2_pass == False:
        score += 1
        pipe2_pass = True
    if x_pipe3 + pipe_width < x_bird and pipe3_pass == False:
        score += 1
        pipe3_pass = True
    screenDown = screen.blit(scratch_Img, (0,600))
    # check col
    pipes = [pipe1, pipe2, pipe3, pipe1_op, pipe2_op, pipe3_op, screenDown]
    for i in pipes:
        if bird.colliderect(i): 
            pygame.mixer.pause()
            pausing = True 
            pipeMoveSpeed = 0
            birdDropVelocity = 0
            gameOverTxt = fontGameOver.render("GAME OVER, Score: "+str(score), True, RED)
            screen.blit(gameOverTxt, (80, 260))
            restartGameTxt = fontGameOver.render("Press Space to restart game", True, RED)
            screen.blit(restartGameTxt, (50, 290))

    for event in pygame.event.get(): # kiểm tra các sự kiện (có thể là có nhận nút quit hay ko/ thao tác với game)
        if event.type == pygame.QUIT: # type lỗ sự kiên, quit nút thoát màn hình  
            running = False
        if event.type == pygame.KEYDOWN:
            running = True
            if event.key == pygame.K_SPACE:
                birdDropVelocity = 0 # reset tốc độ rơi
                birdDropVelocity -= 7 # đưa chi bay lên 1 khoản y = 7
                if pausing:
                    x_bird = 50
                    y_bird = 350
                    x_pipe1 = 400
                    x_pipe2 = 600
                    x_pipe3 = 800
                    pipeMoveSpeed = 2
                    score = 0
                    pausing = False
                    pygame.mixer.unpause()
    # dể tất cả những gì vẽ trên màn hình được hiện thị
    pygame.display.flip()
# sau khi chạy xong trương trình, sd câu lệnh để xóa dữ liệu trg máy
pygame.quit()