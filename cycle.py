from remade_functions import Controller, intersection, Trapezoid, \
    find_min_point, func, area, Rules
import matplotlib.pyplot as plt

g = 9.8
m = 0.5
maxis = 0.01
r = 0.002
R = 0.03
dt = 0.01
T = 50
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
    print(f"xnew = {xnew} vnew = {vnew}")

    return xnew, vnew


data_x = [x0]
data_t = [0]
if __name__ == '__main__':
    lst = []
    x, v = x0, v0
    for i in range(0, int(T / dt)):
        lst = []
        trap = Controller([[x, 1], [v, 1]])

        point_x = intersection(trap.x[0], trap.x[1], Rules.rule_x[0], Rules.rule_x[1])
        point_v = intersection(trap.v[0], trap.v[1], Rules.rule_v[0], Rules.rule_v[1])
        trunc1 = Trapezoid([Rules.w1, find_min_point(point_x, point_v)])
        trunc1.trapezoid()

        point_x2 = intersection(trap.x[0], trap.x[1], Rules.rule_x2[0], Rules.rule_x2[1])
        point_v2 = intersection(trap.v[0], trap.v[1], Rules.rule_v2[0], Rules.rule_v2[1])
        trunc2 = Trapezoid([Rules.w2, find_min_point(point_x2, point_v2)])
        trunc2.trapezoid()

        lst.append(trunc1)
        lst.append(trunc2)
        w = func(lst)
        w = area(w)
        x, v = f(x, v, w)
        # x, v = f(x, v, 0)

        data_x.append(x)
        data_t.append(i)

    fig, ax = plt.subplots()
    ax.plot(data_t, data_x)
    plt.show()
