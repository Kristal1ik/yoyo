from datetime import datetime
import numpy as np
from scipy.optimize import basinhopping
from fuzzy_new import Trapezoid, area
out = 0
global x1, v1, w1, x2, v2, w2, x3, v3, w3, x4, v4, w4, x5, v5, w5
g = 9.8
m = 0.5
maxis = 0.01
r = 0.002
R = 0.03
dt = 0.01
T = 60
l = 0.5
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

    return xnew, vnew


def sorted_four(lst):
    lst_new = []
    lst_fin = []
    for i in range(0, 60, 4):
        lst_new.append(sorted(lst[i:i + 4]))
    for i in lst_new:
        for j in i:
            lst_fin.append(j)
    return lst_fin


def union(x, v, w):
    lst_rules = []
    lst_fin = []
    for i in range(0, 20, 4):
        print(i)
        lst_rules.append([*x[i:i + 4], *v[i:i + 4], *w[i:i + 4]])
    for i in lst_rules:
        for j in i:
            lst_fin.append(j)
    print(lst_fin)
    return lst_fin


class Controller:
    def __init__(self, params):
        global x1, v1, w1, x2, v2, w2, x3, v3, w3, x4, v4, w4, x5, v5, w5
        self.x = Trapezoid([params[0], 0.05, 0.008, 0.008, 0.019, 0]).trapezoid()
        self.v = Trapezoid([params[1], 0.071, 0.0575, 0.0575, 0.15, 0]).trapezoid()
        self.y1 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         x1.a, x1.b, x1.c, x1.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         v1.a, v1.b, v1.c, v1.d)])
        self.y2 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         x2.a, x2.b, x2.c, x2.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         v2.a, v2.b, v2.c, v2.d)])
        self.y3 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         x3.a, x3.b, x3.c, x3.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         v3.a, v3.b, v3.c, v3.d)])
        self.y4 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         x4.a, x4.b, x4.c, x4.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         v4.a, v4.b, v4.c, v4.d)])
        self.y5 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         x5.a, x5.b, x5.c, x5.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         v5.a, v5.b, v5.c, v5.d)])

    def cross_bool(self, b1, c1, b2, c2):
        if b1 > c1:
            b1, c1 = c1, b1
        if b2 > c2:
            b2, c2, = c2, b2
        if b1 > c2:
            b1, b2 = b2, b1
            c1, c2 = c2, c1
        if c1 < b2:
            return False
        else:
            return True

    def intersection(self, a1, b1, c1, d1, a2, b2, c2, d2):
        b = self.cross_bool(b1, c1, b2, c2)
        if b:
            return 1
        if b1 > c2:
            a1, a2 = a2, a1
            b1, b2 = b2, b1
            c1, c2 = c2, c1
            d1, d2 = d2, d1
        b = self.cross_bool(c1, d1, a2, b2)
        if not b:
            return 0
        x = (a2 * c1 - d1 * b2) / (a2 - b2 + c1 - d1)

        return (d1 - x) / (d1 - c1)

    def find_min_point(self, p_xv):
        return min(p_xv)

    def return_(self):
        return self.y1, self.y2, self.y3, self.y4, self.y5


def objective(lst):
    global x1, v1, w1, x2, v2, w2, x3, v3, w3, x4, v4, w4, x5, v5, w5

    start = datetime.now()
    x, v = 0.05, 0
    x1 = Trapezoid([lst[0], lst[1], lst[2], lst[3], 1])
    x1.trapezoid()
    v1 = Trapezoid([lst[4], lst[5], lst[6], lst[7], 1])
    v1.trapezoid()
    w1 = [lst[8], lst[9], lst[10], lst[11], 1]

    # 2 правило
    x2 = Trapezoid([lst[12], lst[13], lst[14], lst[15], 1])
    x2.trapezoid()
    v2 = Trapezoid([lst[16], lst[17], lst[18], lst[19], 1])
    v2.trapezoid()
    w2 = [lst[20], lst[21], lst[22], lst[23], 1]

    # 3 правило
    x3 = Trapezoid([lst[24], lst[25], lst[26], lst[27], 1])
    x3.trapezoid()
    v3 = Trapezoid([lst[28], lst[29], lst[30], lst[31], 1])
    v3.trapezoid()
    w3 = [lst[32], lst[33], lst[34], lst[35], 1]

    # 4 правило
    x4 = Trapezoid([lst[36], lst[37], lst[38], lst[39], 1])
    x4.trapezoid()
    v4 = Trapezoid([lst[40], lst[41], lst[42], lst[43], 1])
    v4.trapezoid()
    w4 = [lst[44], lst[45], lst[46], lst[47], 1]

    # 5 правило
    x5 = Trapezoid([lst[48], lst[49], lst[50], lst[51], 1])
    x5.trapezoid()
    v5 = Trapezoid([lst[52], lst[53], lst[54], lst[55], 1])
    v5.trapezoid()
    w5 = [lst[56], lst[57], lst[58], lst[59], 1]
    counter = 0
    for i in range(1000):
        lst = []
        trap = Controller([[x], [v]]).return_()
        trunc1 = Trapezoid([w1[0], w1[1], w1[2], w1[3], trap[0]]).trapezoid()
        trunc2 = Trapezoid([w2[0], w2[1], w2[2], w2[3], trap[1]]).trapezoid()
        trunc3 = Trapezoid([w3[0], w3[1], w3[2], w3[3], trap[2]]).trapezoid()
        trunc4 = Trapezoid([w4[0], w4[1], w4[2], w4[3], trap[3]]).trapezoid()
        trunc5 = Trapezoid([w5[0], w5[1], w5[2], w5[3], trap[4]]).trapezoid()
        lst.append(trunc1)
        lst.append(trunc2)
        lst.append(trunc3)
        lst.append(trunc4)
        lst.append(trunc5)
        w = area(lst)
        x, v = f(x, v, w)
        global out
        if 0.4 > x > 0.2:
            # print(counter, (datetime.now() - start), lst if (datetime.now() - start).total_seconds() > 10 else None)
            counter += 1
            out += 1
        if out % 10 == 0 and out != 0:
            print(out)
    return -counter



pt_x = np.random.uniform(0.05, 0.5, 20)
pt_x = sorted_four(pt_x)
pt_v = np.random.uniform(-0.08, 0.08, 20)
pt_v = sorted_four(pt_v)
pt_w = np.random.uniform(0, 20.0, 20)
pt_w = sorted_four(pt_w)
pt = union(pt_x, pt_v, pt_w)

# pt = [0.09, 0.14, 0.156, 0.175, 0.280, 0.351, 0.466, 0.616, 6.00, 9.550, 13.550, 16.350,
#       0.270, 0.320, 0.336, 0.355, -0.09, -0.019, 0.096, 0.246, 14.000, 17.550, 21.550, 24.350,
#       0.010, 0.060, 0.076, 0.095, 0.280, 0.351, 0.466, 0.616, 6.000, 9.550, 13.550, 16.350,
#       0.480, 0.530, 0.546, 0.565, 0.730, 0.801, 0.916, 1.066, 20.000, 23.550, 27.550, 30.350,
#       0.270, 0.320, 0.336, 0.355,-0.090, -0.019, 0.096, 0.246, 20.000, 23.550, 27.550, 30.3500]
print(f"len={len(pt)}")
print(objective(pt))
result = basinhopping(objective, pt, stepsize=0.5, niter=5)
print('Status : %s' % result['message'])
print('Total Evaluations: %d' % result['nfev'])
solution = result['x']
evaluation = objective(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))