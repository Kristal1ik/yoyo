import numpy as np


# Центр масс
def area(lst_w):
    dx = 0.1
    integr1 = 0
    integr2 = 0
    for i in np.arange(-1, 30, dx):
        def_h = 0
        for elem in lst_w:
            h = elem.muh(i)
            def_h = max(def_h, h)
            integr1 += def_h * dx * i
            integr2 += def_h * dx
    if integr1 == 0:
        return 0
    try:
        return integr1 / integr2
    except ZeroDivisionError:
        return 0


# Класс нечетких чисел в 2-х мерном пространстве (x, y(h))
class Trapezoid:
    # Фаззификация
    def __init__(self, params):
        if len(params) == 5:
            self.a = params[0]
            self.b = params[1]
            self.c = params[2]
            self.d = params[3]
            self.h = params[4]
        elif len(params) == 6:
            self.a = params[0] - params[1]
            self.b = params[0] - params[2]
            self.c = params[0] + params[3]
            self.d = params[0] + params[4]
            self.h = 1

    # Нахождение соответствующего y для заданного x
    def mu(self, x):
        y = 0
        if (x >= self.a) and (x <= self.b):
            y = 1 - ((self.b - x) / (self.b - self.a))
        elif (x >= self.b) and (x <= self.c):
            y = 1
        elif (x >= self.c) and (x <= self.d):
            y = 1 - ((x - self.c) / (self.d - self.c))
        return y

    # Для центроида
    def muh(self, x):
        return min(self.h, self.mu(x))


# Обработка наблюдаемых значений (x-положение, v=скорость)
class Controller:
    def __init__(self, x, v):
        self.x = Trapezoid([x, 0.05, 0.008, 0.008, 0.019, 0])
        self.v = Trapezoid([v, 0.071, 0.0575, 0.0575, 0.15, 0])
        # self.x = Trapezoid([params[0], 0.55, 0.508, 0.508, 0.519, 0])
        # self.v = Trapezoid([params[1], 0.571, 0.5575, 0.5575, 0.65, 0])
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

    # Нахождение точки пересечкния двух фаззифицированных чисел (x, v)
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

    # Нахождение минимальной точки пересечения
    def find_min_point(self, p_xv):
        return min(p_xv)

    def return_(self):
        return self.y1, self.y2, self.y3, self.y4, self.y5


# Класс правил
class Rules:
    x1 = Trapezoid([0.09, 0.14, 0.156, 0.175, 1])
    v1 = Trapezoid([0.280, 0.351, 0.466, 0.616, 1])
    w1 = [6.00, 9.550, 13.550, 16.350, 1]

    # 2 правило
    x2 = Trapezoid([0.270, 0.320, 0.336, 0.355, 1])
    v2 = Trapezoid([-0.09, -0.019, 0.096, 0.246, 1])
    w2 = [14.000, 17.550, 21.550, 24.350, 1]

    # 3 правило
    x3 = Trapezoid([0.010, 0.060, 0.076, 0.095, 1])
    v3 = Trapezoid([0.280, 0.351, 0.466, 0.616, 1])
    w3 = [6.000, 9.550, 13.550, 16.350, 1]

    # 4 правило
    x4 = Trapezoid([0.480, 0.530, 0.546, 0.565, 1])
    v4 = Trapezoid([0.730, 0.801, 0.916, 1.066, 1])
    w4 = [20.000, 23.550, 27.550, 30.350, 1]

    # 5 правило
    x5 = Trapezoid([0.270, 0.320, 0.336, 0.355, 1])
    v5 = Trapezoid([-0.090, -0.019, 0.096, 0.246, 1])
    w5 = [20.000, 23.550, 27.550, 30.3500, 1]
# x1 = [0.4409094377050431, 0.9402838178072785, 1.0592431525139239, 1.5331502250705729]
# v1 = [0.4497093156328679, 0.5731677729457542, 0.7952094300755321, 1.2381551842526894]
# w1 = [1.8994430457007705, 16.288700694285495, 52.83222705424582, 58.35721370260166]
# x2 = [0.3800030518043793, 0.8419623102159152, 1.0175860227359426, 1.0445410849164567]
# v2 = [0.3617074845502403, 0.41295033188372626, 0.6537170977340352, 0.9820119020370794]
# w2 = [35.56023498893721, 39.773556115053026, 49.878690775921264, 57.34706645304036]
# x3 = [0.43670557717250325, 0.7107881284809644, 1.0598992904554818, 1.2804989700160219]
# v3 = [0.22648432135500113, 0.2872785534447242, 0.4079079880979629, 0.4705149919890135]
# w3 = [8.900892652780957, 33.4166475928893, 49.92263675898375, 76.91767757686733]
# x4 = [0.1601205462729839, 0.3902571145189593, 0.40649271381704427, 0.4608453498130769]
# v4 = [0.44900892652780955, 0.9304074158846418, 1.3758113984893567, 1.5654566262302585]
# w4 = [4.887769893949797, 15.266346227206835, 46.06820782787823, 54.608377203021284]
# x5 = [0.15069810025177385, 0.5202944991226063, 0.9010833905546655, 1.2805981536583504]
# v5 = [0.10736324101625086, 0.43176470588235294, 0.6561684596017395, 0.8697299153124285]
# w5 = [3.851377126726177, 13.807583733882659, 45.319905394064236, 65.50514991989013]
