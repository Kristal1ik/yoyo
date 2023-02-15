import pygame


class Const:
    width = 500
    height = 300
    white = (255, 255, 255)
    # pink = (255, 228, 225)
    pink = (255, 0, 0)
    # beige = (250, 235, 215)
    beige = (0,0,0)
    speed = 5
    r = 20


class YoYo:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


pygame.init()
screen = pygame.display.set_mode((Const.width, Const.height))
pygame.display.set_caption("Yo-Yo")
ball = YoYo(Const.width // 2, Const.height, Const.r)

x_pos = Const.width // 2
y_pos = Const.height
rotate = False
while True:
    screen.fill(Const.white)
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if y_pos <= ball.r:
        rotate = True
    if rotate:
        y_pos += Const.speed

    if not rotate:
        y_pos -= Const.speed
    if y_pos >= Const.height - Const.r:
        rotate = False
    pygame.draw.circle(screen, Const.pink, (x_pos, y_pos), Const.r)
    pygame.draw.line(screen, Const.beige, (x_pos, y_pos - Const.r), (Const.width // 2, 0), 5)

    pygame.display.update()

