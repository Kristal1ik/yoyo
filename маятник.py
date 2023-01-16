import pygame
import sys
import math

pygame.init()
w, h = 600, 600
white = (255, 255, 255)
pink = (255, 228, 225)
bage = (250, 235, 215)
screen = pygame.display.set_mode((w, h))


class Pendulum:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def make(self, screen):
        pygame.draw.circle(screen, pink, (self.x, self.y), self.r)
        pygame.draw.line(screen, bage, (self.x, self.y - self.r), (w // 2, 0), 5)


run = False
lenght = 0
a = 0
v = 0
r = 20
theta = 0
ball = Pendulum(w // 2, 300, r)


def get_anglength():
    lenght = math.sqrt((ball.x - w / 2) ** 2 + (ball.y ** 2))
    theta = math.sin((ball.x - w / 2) / lenght)
    return lenght, theta


def redisplay():
    screen.fill((255, 255, 255))
    ball.make(screen)
    pygame.display.update()


def click(left, right):
    a = 0
    if left:
        a -= 0.01
    if right:
        a += 0.01
    return a


clock = pygame.time.Clock()
while True:
    left = right = False
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            c, d = pygame.mouse.get_pos()
            ball = Pendulum(c, d, r)
            lenght, theta = get_anglength()
            run = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
    if run:
        a = -0.001 * math.sin(theta) + click(left, right)
        v += a
        v *= 0.999
        theta += v
        ball.x = (w / 2 + (lenght * math.sin(theta)))
        ball.y = (lenght * math.cos(theta))
    redisplay()
