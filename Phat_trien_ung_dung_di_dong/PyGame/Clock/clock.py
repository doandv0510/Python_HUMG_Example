import pygame
from time import sleep
import math

pygame.init()

screen = pygame.display.set_mode((500,600)) # set tỉ lệ màn hình 
pygame.display.set_caption("TIMING CLOCK")

# color
BLACK = (0,0,0,0)
WHITE = (255,255,255)
GRAY = (120,120,120)
RED = (250, 0, 0)

# font
fontBtn = pygame.font.SysFont('arial', 50)
textBtn1 = fontBtn.render('+', True, BLACK)
textBtn2 = fontBtn.render('Start', True, BLACK)
textBtn3 = fontBtn.render('-', True, BLACK)
textBtn4 = fontBtn.render('Reset', True, BLACK)

#sound
soundAlart = pygame.mixer.Sound("PyGame/Clock/alarm.mp3")
#tổng giây
totalSecs = 0
total = 0
running = True
start = False
while running:
    screen.fill(GRAY)

    btnPlusMin = pygame.draw.rect(screen, WHITE, (100,50,50,50))
    btnPlusTic = pygame.draw.rect(screen, WHITE, (200,50,50,50))
    btnStart = pygame.draw.rect(screen, WHITE, (300,50,150,50))

    btnMinusMin = pygame.draw.rect(screen, WHITE, (100,200,50,50))
    btnMinusTic = pygame.draw.rect(screen, WHITE, (200,200,50,50))
    btnReset = pygame.draw.rect(screen, WHITE, (300,150,150,50))

    screen.blit(textBtn1, (112,45))
    screen.blit(textBtn1, (212,45))
    screen.blit(textBtn2, (312.2,45))
    screen.blit(textBtn3, (117,193))
    screen.blit(textBtn3, (217,193))
    screen.blit(textBtn4, (317,145))

    pygame.draw.circle(screen, BLACK, (250,400), 100)
    pygame.draw.circle(screen, WHITE, (250,400), 95)
    pygame.draw.circle(screen, BLACK, (250,400), 5)
    
    pygame.draw.rect(screen, BLACK, (50,525,400,50))
    pygame.draw.rect(screen, WHITE, (55,530,390,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos # lấy vị trí của chuột
                if btnPlusMin.collidepoint(mouse_pos): # kiểm tra xem vị trí của chuột có nằm trên nút ko
                    totalSecs += 60
                    total = totalSecs
                elif btnPlusTic.collidepoint(mouse_pos):
                    totalSecs += 1     
                    total = totalSecs    
                elif btnStart.collidepoint(mouse_pos):
                    start = True
                    total = totalSecs
                elif btnMinusMin.collidepoint(mouse_pos):
                    totalSecs -= 60
                    total = totalSecs
                elif btnMinusTic.collidepoint(mouse_pos):
                    totalSecs -= 1
                elif btnReset.collidepoint(mouse_pos):
                    totalSecs = 0
                    soundAlart.stop()

    if start:
        totalSecs-=1
        if totalSecs == 0:
            start = False
            soundAlart.play()
        sleep(1)

    if totalSecs < 0:
        start = False
        totalSecs = 0
    mins = int(totalSecs / 60)
    secs = totalSecs - mins * 60  

    timeNow = str(mins) + " : " + str(secs)  
    textTime = fontBtn.render(timeNow, True, BLACK)      
    screen.blit(textTime, (135,125))

    # vẽ kim giây
    xSec = 250 + 90 * math.sin(6 * secs * math.pi / 180) # lấy tọa độ x điểm đầu của điểm đầu
    ySec = 400 - 90 * math.cos(6 * secs * math.pi / 180) # lấy tọa độ y  điểm đầu của điểm đầu
    pygame.draw.line(screen, BLACK, (250,400), (int(xSec), int(ySec)))# với 4 tọa độ ứng với 2 tọa độ điểm đầu và 2 điểm cuối
   
    xMin = 250 + 40 * math.sin(6 * mins * math.pi / 180)
    yMin = 400 - 40 * math.cos(6 * mins * math.pi / 180)
    pygame.draw.line(screen, RED, (250,400), (int(xMin), int(yMin))) 

    #pro
    if total > 0:
        pygame.draw.rect(screen, RED, (55,530,390 * (totalSecs / total),40))
    pygame.display.flip() # hiển thị tất cả những thứ đã vẽ lên màn hình
pygame.quit()