# def cross_bool(b1, c1, b2, c2):
#     if b1 > c1:
#         b1, c1 = c1, b1
#     if b2 > c2:
#         b2, c2, = c2, b2
#     if b1 > c2:
#         b1, b2 = b2, b1
#         c1, c2 = c2, c1
#     if c1 < b2:
#         return False
#     else:
#         return True
# def cross():
#     a1 = 1
#     b1 = 2
#     c1 = 3
#     d1 = 4
#     a2 = 3
#     b2 = 4.5
#     c2 = 6
#     d2 = 7
#     b = cross_bool(b1, c1, b2, c2)
#     if b:
#         return 1
#     if b1 > c2:
#         a1, a2 = a2, a1
#         b1, b2 = b2, b1
#         c1, c2 = c2, c1
#         d1, d2 = d2, d1
#     b = cross_bool(c1, d1, a2, b2)
#     if not b:
#         return 0
#     x = (a2 * c1 - d1 * b2) / (a2 - b2 + c1 - d1)
#     return (d1 - x) / (d1 - c1)
#
#
# print(cross())
import matplotlib.pyplot as plt

class Trapezoid:
    def __init__(self, params):
        if len(params) == 2:
            n = params[0]
            self.a = n - 2
            self.b = n - 1
            self.c = n + 1
            self.d = n + 2
            self.h = params[1]
        elif len(params) == 5:
            self.a = params[0]
            self.b = params[1]
            self.c = params[2]
            self.d = params[3]
            self.h = params[4]
        self.lst_y = []
        self.lst_x = []
        self.lst_h = []

    def mu(self, x):
        y = 0
        if (x >= self.a) and (x <= self.b):
            y = 1 - ((self.b - x) / (self.b - self.a))
        elif (x >= self.b) and (x <= self.c):
            y = 1
        elif (x >= self.c) and (x <= self.d):
            y = 1 - ((x - self.c) / (self.d - self.c))
        return y

    def trapezoid(self):
        y = 0
        x = 0
        for i in range(5000):
            self.lst_x.append(float(x))
            y = self.mu(x)
            if self.h < 1:
                if float(y) >= self.h:
                    self.lst_h.append(self.h)
                elif float(y) < self.h:
                    self.lst_h.append(y)
                else:
                    self.h = 0
                    self.lst_h.append(self.h)
            self.lst_y.append(float(y))
            x += 0.01
        if self.h < 1:
            self.lst_y = self.lst_h
        return self

    def muh(self, x):
        return min(self.h, self.mu(x))


class Controller:
    def __init__(self, params):
        self.x = Trapezoid(params[0]).trapezoid()
        self.v = Trapezoid(params[1]).trapezoid()
        self.y1 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         Rules.x1.a, Rules.x1.b, Rules.x1.c, Rules.x1.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         Rules.v1.a, Rules.v1.b, Rules.v1.c, Rules.v1.d)])
        self.y2 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         Rules.x2.a, Rules.x2.b, Rules.x2.c, Rules.x2.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         Rules.v2.a, Rules.v2.b, Rules.v2.c, Rules.v2.d)])
        self.y3 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         Rules.x3.a, Rules.x3.b, Rules.x3.c, Rules.x3.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         Rules.v3.a, Rules.v3.b, Rules.v3.c, Rules.v3.d)])
        self.y4 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         Rules.x4.a, Rules.x4.b, Rules.x4.c, Rules.x4.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         Rules.v4.a, Rules.v4.b, Rules.v4.c, Rules.v4.d)])
        self.y5 = min([self.intersection(self.x.a, self.x.b, self.x.c, self.x.d,
                                         Rules.x5.a, Rules.x5.b, Rules.x5.c, Rules.x5.d),
                       self.intersection(self.v.a, self.v.b, self.v.c, self.v.d,
                                         Rules.v5.a, Rules.v5.b, Rules.v5.c, Rules.v5.d)])

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


class Rules:
    x1 = Trapezoid([0.09, 0.14, 0.156, 0.175, 1])
    x1.trapezoid()
    v1 = Trapezoid([0.280, 0.351, 0.466, 0.616, 1])
    v1.trapezoid()
    w1 = [6.00, 9.550, 13.550, 16.350, 1]

    # 2 правило
    x2 = Trapezoid([0.270, 0.320, 0.336, 0.355, 1])
    x2.trapezoid()
    v2 = Trapezoid([-0.09, -0.019, 0.096, 0.246, 1])
    v2.trapezoid()
    w2 = [14.000, 17.550, 21.550, 24.350, 1]

    # 3 правило
    x3 = Trapezoid([0.010, 0.060, 0.076, 0.095, 1])
    x3.trapezoid()
    v3 = Trapezoid([0.280, 0.351, 0.466, 0.616, 1])
    v3.trapezoid()
    w3 = [6.000, 9.550, 13.550, 16.350, 1]

    # 4 правило
    x4 = Trapezoid([0.480, 0.530, 0.546, 0.565, 1])
    x4.trapezoid()
    v4 = Trapezoid([0.730, 0.801, 0.916, 1.066, 1])
    v4.trapezoid()
    w4 = [20.000, 23.550, 27.550, 30.350, 1]

    # 5 правило
    x5 = Trapezoid([0.270, 0.320, 0.336, 0.355, 1])
    x5.trapezoid()
    v5 = Trapezoid([-0.090, -0.019, 0.096, 0.246, 1])
    v5.trapezoid()
    w5 = [20.000, 23.550, 27.550, 30.3500, 1]


def func(lst_m):
    lst_y = []
    x = 0.01
    for i in range(5000):
        lst_y.append(max_f(lst_m, x))
        x += 0.01
    return lst_y


def max_f(list_m, x):
    y = [k.muh(x) for k in list_m]
    return max(y)


def area(lst_w):
    lst_y = func(lst_w)
    integr1 = 0
    integr2 = 0
    x = 0.01
    dx = 0.01
    for i in range(5000):
        integr1 += lst_y[i] * dx * x
        integr2 += lst_y[i] * dx
        x += 0.01
    try:
        integr1 / integr2
    except ZeroDivisionError:
        return 0
    return integr1 / integr2



if __name__ == '__main__':
    trap = Controller([[0.05, 1], [0, 1]]).return_()
    lst = []
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
    print(w)
    plt.subplot()
    plt.plot(trunc1.lst_x, trunc1.lst_y, trunc2.lst_x, trunc2.lst_y,
             trunc3.lst_x, trunc3.lst_y,trunc4.lst_x, trunc4.lst_y, trunc5.lst_x, trunc5.lst_y)
    plt.scatter(w, 0)
    plt.show()
