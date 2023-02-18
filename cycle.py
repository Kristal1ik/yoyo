from remade_functions import Controller, intersection, Trapezoid, \
    find_min_point, func, area, Rules
import matplotlib.pyplot as plt

g = 9.8
m = 0.5
maxis = 0.01
r = 0.002
R = 0.03
dt = 0.01
T = 30
x0 = 0.05
v0 = 0
l = 0.5
x1 = 0.2
x2 = 0.3
F1 = -20
F2 = 20
k = 0.1
e = 0.000001


def f(x, v, w):
    a = (m * r * r * (g - w)) / (0.5 * (m * R * R + maxis * r * r) + (m + maxis) * r * r)
    if (x == R and v < 0) or (x == l and v > 0):
        v = -v * (1 - k)
    xnew = x + v * dt + 0.5 * dt ** 2 * a
    vnew = v + a * dt
    if xnew > l:
        xnew = l
    if xnew < R:
        xnew = R
    # print(f"xnew = {xnew} vnew = {vnew}")

    return xnew, vnew


data_x = [x0]
data_t = [0]
if __name__ == '__main__':
    lst = []
    x, v = x0, v0
    for i in range(0, int(T / dt)):
        lst = []
        trap = Controller([[x, 1], [v, 1]])

        point_x = intersection(trap.x[0], trap.x[1], Rules.x1[0], Rules.x1[1])
        point_v = intersection(trap.v[0], trap.v[1], Rules.v1[0], Rules.v1[1])
        trunc1 = Trapezoid([Rules.w1[0], Rules.w1[1], Rules.w1[2], Rules.w1[3], find_min_point(point_x, point_v)])
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
        trunc4 = Trapezoid([Rules.w4[0], Rules.w4[1], Rules.w4[1], Rules.w4[3], find_min_point(point_x4, point_v4)])
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
        x, v = f(x, v, w)
        # x, v = f(x, v, 0)

        data_x.append(x)
        data_t.append(i)

    fig, ax = plt.subplots()
    ax.plot(data_t, data_x)
    plt.show()
