import pygame # import thư viện
from random import randint

widthScreen = 400
heightScreen = 670
#color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((widthScreen,heightScreen))
pygame.display.set_caption('Flappy Bird'); 
clock = pygame.time.Clock();
FPS = 60

#background
backGroundImg = pygame.image.load("FlappyBird/Resource/images/background-night.png")
backGroundImg = pygame.transform.scale(backGroundImg,(widthScreen,heightScreen-70))

#bottom background
baseImg = pygame.image.load('FlappyBird/Resource/images/base.png')
baseImg = pygame.transform.scale(baseImg,(widthScreen,heightScreen-600))

#bird
xBird = 50
yBird = 350
birdImg = pygame.image.load('FlappyBird/Resource/images/bird3.png')
birdImg = pygame.transform.scale(birdImg,(45, 35))

# pipes
xPipe1 = 300
xPipe2 = 500
xPipe3 = 700
pipe_width = 50 # chiều rộng các ống bằng nhau
pipe1Height = randint(100,400) # chiều cao các ống chạy ngẫu nhiêu từ 100->400
pipe2Height = randint(100,400)
pipe3Height = randint(100,400)
#check pass 3 pipe
pipe1Pass = False
pipe2Pass = False
pipe3Pass = False
# pipeImg
pipeImg = pygame.image.load("FlappyBird/Resource/images/tube.png")
pipeOpImg = pygame.image.load("FlappyBird/Resource/images/tube_op.png")
hole2pipe = 150
birdDropSpeed = 0 
gravity = 0.5
pipeMoveSpeed = 2
backgroundMoveSpeed = 2
xBg = 0
score = 0
fontScore = pygame.font.SysFont('arial', 50)
fontGameOver = pygame.font.SysFont('arial', 30)

running = True  
gameover = False 

def soundPointPlay():
    pygame.mixer.music.load('FlappyBird/Resource/point.mp3')
    pygame.mixer.music.play(1)

def gameOver():
    gameOverTxt = fontGameOver.render("GAME OVER, Score: "+str(score), True, BLACK)
    screen.blit(gameOverTxt, (80, 260))
    restartGameTxt = fontGameOver.render("Press Space to restart game", True, BLACK)
    screen.blit(restartGameTxt, (50, 290))
    s=pygame.mixer.Sound("FlappyBird/Resource/hit.mp3")        
    s.play()
    import time
    time.sleep(1)
    s.stop()
    
while running:
    clock.tick(FPS) 
    # screen.fill(WHITE)  

    rel_x = xBg % backGroundImg.get_rect().width
    backGround = screen.blit(backGroundImg,(rel_x - backGroundImg.get_rect().width,0))
    bottomBackgound = screen.blit(baseImg,(rel_x - backGroundImg.get_rect().width,600))
    if rel_x < 400:
        screen.blit(backGroundImg, (rel_x, 0))
        screen.blit(baseImg, (rel_x, 600))
    xBg -= backgroundMoveSpeed
    
    # tạo ra các ống
    pipe1Img = pygame.transform.scale(pipeImg,(pipe_width, pipe1Height))
    pipe1 =  screen.blit(pipe1Img,(xPipe1, 0))
    
    pipe2Img = pygame.transform.scale(pipeImg,(pipe_width, pipe2Height))
    pipe2 = screen.blit(pipe2Img, (xPipe2, 0))

    pipe3Img = pygame.transform.scale(pipeImg,(pipe_width, pipe3Height))
    pipe3 = screen.blit(pipe3Img, (xPipe3, 0))
    
    # tạo ra các ống đối diện với ống phía trên
    pipe1OpImg = pygame.transform.scale(pipeOpImg,(pipe_width, heightScreen-70-(pipe1Height +  hole2pipe)))
    pipe1Op =  screen.blit(pipe1OpImg,(xPipe1, pipe1Height +  hole2pipe)) 

    pipe2OpImg = pygame.transform.scale(pipeOpImg,(pipe_width, heightScreen-70-(pipe2Height +  hole2pipe)))
    pipe2Op =  screen.blit(pipe2OpImg,(xPipe2, pipe2Height +  hole2pipe)) 
    
    pipe3OpImg = pygame.transform.scale(pipeOpImg,(pipe_width, heightScreen-70-(pipe3Height +  hole2pipe)))
    pipe3Op =  screen.blit(pipe3OpImg,(xPipe3, pipe3Height +  hole2pipe))

    xPipe1 -= pipeMoveSpeed
    xPipe2 -= pipeMoveSpeed
    xPipe3 -= pipeMoveSpeed
    
    # tạo lại ống mới
    if(xPipe1 < -pipe_width): 
        xPipe1 = 550
        pipe1Height = randint(100,400)
        pipe1Pass = False
    if(xPipe2 < -pipe_width):
        xPipe2 = 550
        pipe2Height = randint(100,400)
        pipe2Pass = False
    if(xPipe3 < -pipe_width):
        xPipe3 = 550
        pipe3Height = randint(100,400) 
        pipe3Pass = False

    # vẽ chim
    bird = screen.blit(birdImg,(xBird, yBird))
    yBird = yBird + birdDropSpeed
    birdDropSpeed += gravity
    
    # hiển thi điểm
    printScore = fontScore.render(""+ str(score), True, RED)
    screen.blit(printScore, (182,90))
    # ghi điểm
    if xPipe1 + pipe_width < xBird and pipe1Pass == False:
        score += 1
        pipe1Pass = True
        soundPointPlay()
    if xPipe2 + pipe_width < xBird and pipe2Pass == False:
        score += 1
        pipe2Pass = True
        soundPointPlay()
    if xPipe3 + pipe_width < xBird and pipe3Pass == False:
        score += 1
        pipe3Pass = True
        soundPointPlay()
    
    
    # check col
    pipes = [pipe1, pipe2, pipe3, pipe1Op, pipe2Op, pipe3Op]
    for i in pipes:
        if bird.colliderect(i):
            gameover = True 
            backgroundMoveSpeed = 0
            pipeMoveSpeed = 0
            birdDropSpeed = 0
            gameOver()
    if yBird <= 0 or yBird >= 560:
        gameover = True 
        backgroundMoveSpeed = 0
        pipeMoveSpeed = 0
        birdDropSpeed = 0
        gameOver()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            running = True
            if event.key == pygame.K_SPACE:  
                pygame.mixer.music.load("FlappyBird/Resource/wing.mp3")
                pygame.mixer.music.play(1)
                birdDropSpeed = 0
                birdDropSpeed -= 7 
                if gameover:
                    xBird = 50
                    yBird = 350
                    xPipe1 = 400
                    xPipe2 = 600
                    xPipe3 = 800
                    pipeMoveSpeed = 2
                    backgroundMoveSpeed = 2
                    score = 0
                    gameover = False
    pygame.display.flip() 
pygame.quit() 