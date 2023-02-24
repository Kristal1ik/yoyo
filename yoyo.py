import pygame
from remade_functions import Controller, intersection, Trapezoid, \
    find_min_point, func, area, Rules


class Const:
    width = 1300
    height = 650
    white = (255, 255, 255)
    # pink = (255, 228, 225)
    pink = (255, 0, 0)
    # beige = (250, 235, 215)
    beige = (0, 0, 255)
    speed = 5
    r = 7.5590551181
    g = 9.8
    m = 0.5
    maxis = 0.01
    R = 113.38582677
    dt = 0.01
    T = 60
    x0 = 0.05
    v0 = 0
    l = 1889.7637795
    k = 0.1


def f(x, v, w):
    a = (Const.m * Const.r * Const.r * (Const.g - w)) / (
                0.5 * (Const.m * Const.R * Const.R + Const.maxis * Const.r * Const.r) + (
                    Const.m + Const.maxis) * Const.r * Const.r)
    if (x == Const.R and v < 0) or (x == Const.l and v > 0):
        v = -v * (1 - Const.k)
    xnew = x + v * Const.dt + 0.5 * Const.dt ** 2 * a
    vnew = v + a * Const.dt
    if xnew > Const.l:
        xnew = Const.l
    if xnew < Const.R:
        xnew = Const.R
    print(f"xnew = {xnew} vnew = {vnew}")

    return xnew, vnew


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
rotate = False
y_pos, v = Const.x0, Const.v0
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

    print(y_pos)
    # lst = []
    # trap = Controller([[y_pos, 1], [v, 1]])
    #
    # point_x = intersection(trap.x[0], trap.x[1], Rules.rule_x[0], Rules.rule_x[1])
    # point_v = intersection(trap.v[0], trap.v[1], Rules.rule_v[0], Rules.rule_v[1])
    # trunc1 = Trapezoid([Rules.w1, find_min_point(point_x, point_v)])
    # trunc1.trapezoid()
    #
    # point_x2 = intersection(trap.x[0], trap.x[1], Rules.rule_x2[0], Rules.rule_x2[1])
    # point_v2 = intersection(trap.v[0], trap.v[1], Rules.rule_v2[0], Rules.rule_v2[1])
    # trunc2 = Trapezoid([Rules.w2, find_min_point(point_x2, point_v2)])
    # trunc2.trapezoid()
    #
    # lst.append(trunc1)
    # lst.append(trunc2)
    # w = func(lst)
    # w = area(w)
    # print(w)
    # y_pos, v = f(y_pos, v, w)
    pygame.draw.circle(screen, Const.pink, (int(x_pos), int(y_pos)), Const.r)
    pygame.draw.line(screen, Const.beige, (int(x_pos), int(y_pos) - Const.r), (int(Const.width // 2), 0), int(v))

    pygame.display.update()
