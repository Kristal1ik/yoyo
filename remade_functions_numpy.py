from random import randint
import numpy as np


# y = kx + b
# k = (y - b) / x
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k*x2

class Trapezoid:
    def __init__(self, params):
        n = params[0]
        self.a = n - 2
        self.b = n - 1
        self.c = n + 1
        self.d = n + 2
        self.h = params[1]
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
        x = 0.01
        for i in range(1000):
            self.lst_x.append(float(x))
            y = self.mu(x)
            x += 0.01
            if self.h < 1:
                if float(y) >= self.h:
                    self.lst_h.append(self.h)
                elif float(y) < self.h:
                    self.lst_h.append(y)
                else:
                    self.h = 0
                    self.lst_h.append(self.h)
            self.lst_y.append(float(y))
        if self.h < 1:
            self.lst_y = self.lst_h
        return self.lst_x, self.lst_y

    def muh(self, x):
        return min(self.h, self.mu(x))


# Нахождение максимального значения y
def func(lst_m):
    lst_y = []
    x = 0.01
    for i in range(1000):
        lst_y.append(max_f(lst_m, x))
        x += 0.01
    # print(lst_y)
    return lst_y


def max_f(list_m, x):
    y = [k.muh(x) for k in list_m]
    return max(y)


def area(lst_y):
    integr1 = 0
    integr2 = 0
    x = 0.01
    dx = 0.01
    for i in range(1000):
        integr1 += lst_y[i] * dx * x
        integr2 += lst_y[i] * dx
        x += 0.01
    return integr1 / integr2


# Нахождение точки пересечения (y, x)
def intersection(one_x, one_y, two_x, two_y):
    lst_intersection = []
    x = 0.01
    temp1 = 0
    for i in range(1000):
        if round(one_y[i], 2) == round(two_y[i], 2) and one_y[i] != 0 and two_y != 0:
            lst_intersection.append([one_y[i], one_x[i]])
        else:
            lst_intersection.append([0,0])
        x += 0.01
    print(temp1)
    max_y = max(lst_intersection)
    return max_y[::-1]


def find_min_point(p_x, p_v):
    if p_x[1] < p_v[1]:
        return p_x[1]
    return p_v[1]


class Controller:
    def __init__(self, params):
        self.x = Trapezoid(params[0]).trapezoid()
        self.v = Trapezoid(params[1]).trapezoid()
class Rules:
    w_fin = 3
    w_1 = 7
    w_2 = 8
    rule_x = Trapezoid([5.5, 1]).trapezoid()
    rule_v = Trapezoid([5, 1]).trapezoid()
    rule_w = Trapezoid([w_1, 1]).trapezoid()
    rule_w_2 = Trapezoid([w_2, 1]).trapezoid()

class Rules_consts:
    w = randint(1, 9)
    v = randint(1, 9)
    x = randint(1, 9)


def rules(n):
    w_1 = []
    rule_x = []
    rule_v = []
    for i in range(n):
        rule_x.append(Trapezoid([Rules_consts.x, 1]).trapezoid())
        rule_v.append(Trapezoid([Rules_consts.v, 1]).trapezoid())
        w_1.append(Trapezoid([Rules_consts.w, 1]).trapezoid())
    return rule_x, rule_v, w_1

def making_rules(n):
    point_x = []
    point_v = []
    lst = []
    for i in range(n):
        lst_rules = []
        for i in range(2):
            rule = list(map(int, input().split()))
            lst_rules.append(rule)

        lst_rules = Controller(lst_rules)
        point_x = intersection(lst_rules.x[0], lst_rules.x[1], Rules.rule_x[0], Rules.rule_x[1])
        point_v = intersection(lst_rules.v[0], lst_rules.v[1], Rules.rule_v[0], Rules.rule_v[1])
        trunc1 = Trapezoid([3, find_min_point(point_x, point_v)])
        trunc1.trapezoid()
        lst.append(trunc1)
    f = func(lst)
    ff = area(f)
    print(ff)
    return ff