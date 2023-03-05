from fuzzy_new import Rules, Controller, Trapezoid, area
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
    print(f"xnew = {xnew} vnew = {vnew}")

    return xnew, vnew


data_x = [x0]
data_t = [0]
if __name__ == '__main__':
    lst = []
    x, v = x0, v0
    for i in range(0, int(T / dt)):
        lst = []
        trap = Controller([[0.05, 1], [0, 1]]).return_()
        trunc1 = Trapezoid([Rules.w1[0], Rules.w1[1], Rules.w1[2], Rules.w1[3], trap[0]]).trapezoid()
        trunc2 = Trapezoid([Rules.w2[0], Rules.w2[1], Rules.w2[2], Rules.w2[3], trap[1]]).trapezoid()
        trunc3 = Trapezoid([Rules.w3[0], Rules.w3[1], Rules.w3[2], Rules.w3[3], trap[2]]).trapezoid()
        trunc4 = Trapezoid([Rules.w4[0], Rules.w4[1], Rules.w4[2], Rules.w4[3], trap[3]]).trapezoid()
        trunc5 = Trapezoid([Rules.w5[0], Rules.w5[1], Rules.w5[2], Rules.w5[3], trap[4]]).trapezoid()
        lst.append(trunc1)
        lst.append(trunc2)
        lst.append(trunc3)
        lst.append(trunc4)
        lst.append(trunc5)
        w = area(lst)
        # x, v = f(x, v, w)
        x, v = f(x, v, 0)
        print(w)
        data_x.append(x)
        data_t.append(i)

    fig, ax = plt.subplots()
    ax.plot(data_t, data_x)
    plt.show()
