import datetime
import  pygame
import  math
pygame.init()

display = pygame.display.set_mode((700,700))
pygame.display.set_caption("clock")
clock = pygame.time.Clock()
FPS =50
def print_text(text, positon):
    font = pygame.font.SysFont("Castellar", 40,True, False )
    surface = font.render(text,(True),(0,0,0))
    display.blit(surface,positon)


def covert_degrees_to_pygame(R,theta):
    y = math.cos(2 * math.pi * theta / 360) *R
    x = math.sin(2 * math.pi * theta / 360) * R
    return x+350-15,-(y-350)-15

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        curren_time = datetime.datetime.now()
        seconds = curren_time.second
        minute = curren_time.minute
        housr = curren_time.hour

        display.fill(((255,255,255)))
        pygame.draw.circle(display,(0,0,0),(350,350),350,4)

        for number in range(1,13):
            print_text(str(number), covert_degrees_to_pygame(325, number*30))

        R = 320
        theta = seconds*(360/60)
        pygame.draw.line(display,(0,0,0),(350,350), covert_degrees_to_pygame(R,theta), 8 )
        R = 300
        theta =minute*(360/60)
        pygame.draw.line(display,(255,0,0),(350,350), covert_degrees_to_pygame(R,theta), 8 )
        R = 250
        theta = housr*(360/12)
        pygame.draw.line(display,(0,0,0),(350,350), covert_degrees_to_pygame(R,theta), 8 )
        pygame.display.update()
        clock.tick(FPS)
game()
pygame.quit()