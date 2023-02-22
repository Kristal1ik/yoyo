import random

g = 9.8
m = 0.5
maxis = 0.01
r = 0.002
R = 0.03
dt = 0.01
T = 60
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
    y_new = x + v * dt + 0.5 * dt ** 2 * a
    v_new = v + a * dt
    if y_new > l:
        y_new = l
    if y_new < R:
        y_new = R
    return y_new, v_new
# 
# 
# data_x = [x0]
# data_t = [0]
# 
# x, v = x0, v0
# for i in range(0, int(T / dt)):
#     w = random.uniform(-10, 10)
#     x, v = f(x, v, 0)
#     data_x.append(x)
#     data_t.append(i)
# 
# import matplotlib.pyplot as plt
# 
# fig, ax = plt.subplots()
# ax.plot(data_t, data_x)
# plt.show()
