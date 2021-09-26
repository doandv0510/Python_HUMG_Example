import pygame
import sys, os

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
#define display surface
Width, Height = 400, 670
HW, HH = Width/2, Height/2
AREA = Width * Height

#setting pygame
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((Width, Height))
FPS = 120
backGroundImg = pygame.image.load("PyGame/FlappyBird/Resource/images/backgroundImageFlappyBirrd.png")
backGroundImg = pygame.transform.scale(backGroundImg,(900,600))
x = 0

running = True
while running:
    event()

    rel_x = x % backGroundImg.get_rect().width
    screen.blit(backGroundImg, (rel_x - backGroundImg.get_rect().width,0))
    if rel_x < Width:
        screen.blit(backGroundImg, (rel_x,0))
    x -= 1
    pygame.display.update()
    CLOCK.tick(FPS)
