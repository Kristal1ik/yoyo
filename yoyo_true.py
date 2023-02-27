import pygame
from remade_functions_numpy import Controller, intersection, Trapezoid, \
    find_min_point, func, area, Rules


class Const:
    width = 1300
    height = 650
    white = (255, 255, 255)
    # pink = (255, 228, 225)
    pink = (255, 0, 0)
    # beige = (250, 235, 215)
    beige = (0, 0, 255)
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
    ynew = x + v * Const.dt + 0.5 * Const.dt ** 2 * a
    vnew = v + a * Const.dt
    if ynew > Const.l:
        ynew = Const.l
    if ynew < Const.R:
        ynew = Const.R
    print(f"ynew = {ynew} vnew = {vnew}")

    return ynew, vnew * 10


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
    print(y_pos)
    lst = []
    trap = Controller([[y_pos, 1], [v, 1]])
    point_x1 = intersection(trap.x[0], trap.x[1], Rules.x1[0], Rules.x1[1])
    point_v1 = intersection(trap.v[0], trap.v[1], Rules.v1[0], Rules.v1[1])
    print(point_v1)
    trunc1 = Trapezoid([Rules.w1[0], Rules.w1[1], Rules.w1[2], Rules.w1[3], find_min_point(point_x1, point_v1)])
    trunc1.trapezoid()


    point_x2 = intersection(trap.x[0], trap.x[1], Rules.x2[0], Rules.x2[1])
    point_v2 = intersection(trap.v[0], trap.v[1], Rules.v2[0], Rules.v2[1])

    trunc2 = Trapezoid([Rules.w2[0], Rules.w2[1], Rules.w2[2], Rules.w2[3], find_min_point(point_x2, point_v2)])
    trunc2.trapezoid()

    point_x3 = intersection(trap.x[0], trap.x[1], Rules.x3[0], Rules.x3[1])
    point_v3 = intersection(trap.v[0], trap.v[1], Rules.v3[0], Rules.v3[1])
    trunc3 = Trapezoid([Rules.w3[0], Rules.w3[1], Rules.w3[2], Rules.w3[3], find_min_point(point_x3, point_v3)])
    trunc3.trapezoid()

    point_x4 = intersection(trap.x[0], trap.x[1], Rules.x4[0], Rules.x4[1])
    point_v4 = intersection(trap.v[0], trap.v[1], Rules.v4[0], Rules.v4[1])
    trunc4 = Trapezoid([Rules.w4[0], Rules.w4[1], Rules.w4[2], Rules.w4[3], find_min_point(point_x4, point_v4)])
    trunc4.trapezoid()

    point_x5 = intersection(trap.x[0], trap.x[1], Rules.x5[0], Rules.x5[1])
    point_v5 = intersection(trap.v[0], trap.v[1], Rules.v5[0], Rules.v5[1])
    trunc5 = Trapezoid([Rules.w5[0], Rules.w5[1], Rules.w5[2], Rules.w5[3], find_min_point(point_x5, point_v5)])
    trunc5.trapezoid()

    lst.append(trunc1)
    lst.append(trunc2)
    lst.append(trunc3)
    lst.append(trunc4)
    lst.append(trunc5)
    w = func(lst)
    w = area(w)
    print(w)
    y_pos, v = f(y_pos, v, w)


    pygame.draw.circle(screen, Const.pink, (int(x_pos), int(y_pos)), Const.r)
    pygame.draw.line(screen, Const.beige, (int(x_pos), int(y_pos) - Const.r), (int(Const.width // 2), 0), int(v))

    pygame.display.update()
