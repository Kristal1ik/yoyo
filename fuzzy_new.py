class Trapezoid:
    def __init__(self, params):
        if len(params) == 2:
            n = params[0]
            self.a = n - 0.4
            self.b = n - 0.2
            self.c = n + 0.2
            self.d = n + 0.4
            self.h = params[1]
        elif len(params) == 5:
            self.a = params[0]
            self.b = params[1]
            self.c = params[2]
            self.d = params[3]
            self.h = params[4]
        elif len(params) == 6:
            self.a = params[0][0] - params[1]
            self.b = params[0][0] - params[2]
            self.c = params[0][0] + params[3]
            self.d = params[0][0] + params[4]
            self.h = 1
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
        self.x = Trapezoid([params[0], 0.05, 0.008, 0.008, 0.019, 0]).trapezoid()
        self.v = Trapezoid([params[1], 0.071, 0.0575, 0.0575, 0.15, 0]).trapezoid()
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
    x1 = Trapezoid([3.72535124e-01,  1.39610131e-01,  2.56110037e-01,  5.93458773e-01, 1])
    x1.trapezoid()
    v1 = Trapezoid([-2.91267924e-01, -3.07721294e-01,  3.38680508e-01,  4.21451555e-01, 1])
    v1.trapezoid()
    w1 = [1.96757455e-02,  3.86573069e+00,  4.73863930e+00,  1.90367415e+01, 1]

    # 2 правило
    x2 = Trapezoid([3.98411566e-01, -3.92452678e-02 , 4.69438036e-02,  4.57678197e-01, 1])
    x2.trapezoid()
    v2 = Trapezoid([5.21865876e-02, -5.11420042e-01, -4.03177720e-01, -4.59437151e-03, 1])
    v2.trapezoid()
    w2 = [6.34066447e-01,  3.57999561e+00,  1.07309511e+01,  1.94137837e+01, 1]

    # 3 правило
    x3 = Trapezoid([1.35109638e-01,  2.68685584e-01,  1.24704081e-01,  5.69131503e-01, 1])
    x3.trapezoid()
    v3 = Trapezoid([-1.18142037e-01, -3.25285366e-01,  2.34673317e-01, -1.71587548e-01, 1])
    v3.trapezoid()
    w3 = [1.64632774e+00,  7.86960641e+00,  1.38785216e+01,  1.47364825e+01, 1]


    # 4 правило
    x4 = Trapezoid([-3.64730409e-01,  5.73097395e-01, -9.02278758e-02,  9.75379871e-01, 1])
    x4.trapezoid()
    v4 = Trapezoid([-3.17735156e-01, -4.68277672e-01, -3.25724280e-01,  2.71852384e-01, 1])
    v4.trapezoid()
    w4 = [-5.33154609e-04,  1.84698090e+00,  8.06121151e+00,  1.09809382e+01, 1]

    # 5 правило
    x5 = Trapezoid([2.07328571e-01,  3.02712824e-01,  3.77895285e-01,  2.39740504e-01, 1])
    x5.trapezoid()
    v5 = Trapezoid([4.33301113e-01, -2.94739201e-01,  4.20622828e-02,  5.10592489e-01, 1])
    v5.trapezoid()
    w5 = [7.72609707e-01,  1.96710107e+00,  7.10901018e+00,  1.45310929e+01, 1]
# class Rules:
#     x1 = Trapezoid([9.000e-02,  1.400e-01,  1.560e-01,  1.750e-01, 1])
#     x1.trapezoid()
#     v1 = Trapezoid([2.800e-01,  3.510e-01, 4.660e-01,  6.160e-01, 1])
#     v1.trapezoid()
#     w1 = [6.000e+00,  9.550e+00,  1.355e+01, 1.635e+01, 1]
#
#     # 2 правило
#     x2 = Trapezoid([2.700e-01, 3.200e-01, 3.360e-01, 3.550e-01, 1])
#     x2.trapezoid()
#     v2 = Trapezoid([-9.000e-02, -1.900e-02, 9.600e-02,  2.460e-01, 1])
#     v2.trapezoid()
#     w2 = [1.400e+01,  1.755e+01,  2.155e+01,  2.435e+01, 1]
#
#     # 3 правило
#     x3 = Trapezoid([1.000e-02, 6.000e-02,  7.600e-02,  9.500e-02, 1])
#     x3.trapezoid()
#     v3 = Trapezoid([2.800e-01,  3.510e-01, 4.660e-01,  6.160e-01, 1])
#     v3.trapezoid()
#     w3 = [6.000e+00,  9.550e+00,  1.355e+01,  1.635e+01, 1]
#
#
#     # 4 правило
#     x4 = Trapezoid([4.800e-01,  5.300e-01,  5.460e-01,  5.650e-01, 1])
#     x4.trapezoid()
#     v4 = Trapezoid([7.300e-01,  8.010e-01, 9.160e-01,  1.066e+00, 1])
#     v4.trapezoid()
#     w4 = [2.000e+01,  2.355e+01,  2.755e+01,  3.035e+01, 1]
#
#     # 5 правило
#     x5 = Trapezoid([2.700e-01,  3.200e-01,  3.360e-01,  3.550e-01, 1])
#     x5.trapezoid()
#     v5 = Trapezoid([-9.000e-02, -1.900e-02, 9.600e-02,  2.460e-01, 1])
#     v5.trapezoid()
#     w5 = [2.000e+01,  2.355e+01,  2.755e+01,  3.035e+01, 1]


# class Rules:
#     x1 = Trapezoid([0.09, 0.14, 0.156, 0.175, 1])
#     x1.trapezoid()
#     v1 = Trapezoid([0.280, 0.351, 0.466, 0.616, 1])
#     v1.trapezoid()
#     w1 = [6.00, 9.550, 13.550, 16.350, 1]
#
#     # 2 правило
#     x2 = Trapezoid([0.270, 0.320, 0.336, 0.355, 1])
#     x2.trapezoid()
#     v2 = Trapezoid([-0.09, -0.019, 0.096, 0.246, 1])
#     v2.trapezoid()
#     w2 = [14.000, 17.550, 21.550, 24.350, 1]
#
#     # 3 правило
#     x3 = Trapezoid([0.010, 0.060, 0.076, 0.095, 1])
#     x3.trapezoid()
#     v3 = Trapezoid([0.280, 0.351, 0.466, 0.616, 1])
#     v3.trapezoid()
#     w3 = [6.000, 9.550, 13.550, 16.350, 1]
#
#
#     # 4 правило
#     x4 = Trapezoid([0.480, 0.530, 0.546, 0.565, 1])
#     x4.trapezoid()
#     v4 = Trapezoid([0.730, 0.801, 0.916, 1.066, 1])
#     v4.trapezoid()
#     w4 = [20.000, 23.550, 27.550, 30.350, 1]
#
#     # 5 правило
#     x5 = Trapezoid([0.270, 0.320, 0.336, 0.355, 1])
#     x5.trapezoid()
#     v5 = Trapezoid([-0.090, -0.019, 0.096, 0.246, 1])
#     v5.trapezoid()
#     w5 = [20.000, 23.550, 27.550, 30.3500, 1]


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
# 4.18146640e-01 -1.79497512e-01  8.70269649e-02  3.03605818e-02
#  -4.16378341e-01 -7.02737886e-02 -1.64044628e-01 -1.19823955e-01
#   4.13621014e+00  6.54102338e+00  9.84232245e+00  1.40241447e+01
#  -2.50078058e-01 -6.12273210e-03  2.85736156e-01 -4.67160251e-02
#   2.77949506e-01 -1.22649861e-01  1.62101339e-01  4.21372881e-01
#   7.83600279e-01  2.34639689e+00  5.78330644e+00  1.59383212e+01
#  -2.73647487e-01  4.42686194e-01 -1.17028443e-01  1.13545814e-01
#  -4.97731466e-01  3.85085132e-01 -2.33416664e-01  2.35434833e-01
#   7.17782751e-01  1.08587348e+00  6.84135410e+00  1.08201027e+01
#   1.06229987e-01 -2.17359783e-02  1.21964888e-01  5.31392736e-01
#   4.18709429e-01 -3.02583499e-01  4.51610717e-01 -2.40911794e-01
#   9.31468738e-01  3.06607083e+00  1.28034116e+01  1.92613045e+01
#  -4.08816955e-01  3.17998779e-01  4.83229377e-01  6.91891148e-01
#   1.93770182e-01 -1.15794876e-01 -3.73195570e-01  4.69588296e-01
#   3.13099570e+00  5.77091427e+00  1.02507205e+01  1.31139935e+01