import matplotlib.pyplot as plt


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
            print("ds")
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
    return lst_y


def max_f(list_m, x):
    y = [k.mu(x) for k in list_m]
    return max(y)


def area(lst_y):
    s = 0
    x = 0.01
    dx = 0.01
    for i in range(1000):
        s += lst_y[i] * dx
        x += 0.01
    return s


# Нахождение точки пересечения (y, x)
def intersection(one_x, one_y, two_x, two_y):
    lst_intersection = []
    x = 0.01
    for i in range(1000):
        if round(one_y[i], 2) == round(two_y[i], 2) and one_y[i] != 0 and two_y != 0:
            lst_intersection.append([one_y[i], one_x[i]])
        x += 0.01
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
    w_fin = 6
    w_1 = 3
    w_2 = 5
    rule_x = Trapezoid([5.5, 1]).trapezoid()
    rule_v = Trapezoid([5, 1]).trapezoid()
    rule_w = Trapezoid([w_1, 1]).trapezoid()
    rule_w_2 = Trapezoid([w_2, 1]).trapezoid()



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
    print(lst)
    f = func(lst)
    f = area(f)
    return f


#     min_a = 2
#     max_d = -0.5
#     for i in lst_m:
#         if i.a < min_a:
#             min_a = i.a
#         if i.d > max_d:
#             max_d = i.d
#     return min_a, max_d


if __name__ == '__main__':
    trap = Controller([[2, 1], [7, 1]])
    point_x = intersection(trap.x[0], trap.x[1], Rules.rule_x[0], Rules.rule_x[1])
    plt.subplot(241)
    plt.plot(trap.x[0], trap.x[1], 'b', Rules.rule_x[0], Rules.rule_x[1], 'r')
    plt.scatter(point_x[0], point_x[1], color="#7B68EE")

    point_v = intersection(trap.v[0], trap.v[1], Rules.rule_v[0], Rules.rule_v[1])
    plt.subplot(242)
    plt.plot(trap.v[0], trap.v[1], 'b', Rules.rule_v[0], Rules.rule_v[1], 'r')
    plt.scatter(point_v[0], point_v[1], color="#7B68EE")
    print(point_v)

    plt.subplot(243)
    trunc1 = Trapezoid([Rules.w_1, find_min_point(point_x, point_v)])
    trunc1.trapezoid()
    plt.plot(Rules.rule_w[0], trunc1.lst_y, 'g', Rules.rule_w[0], Rules.rule_w[1])

    trap2 = Controller([[5, 1], [2, 1]])

    point_x2 = intersection(trap2.x[0], trap2.x[1], Rules.rule_x[0], Rules.rule_x[1])
    plt.subplot(245)
    plt.plot(trap2.x[0], trap2.x[1], 'b', Rules.rule_x[0], Rules.rule_x[1], 'r')
    plt.scatter(point_x2[0], point_x2[1], color="#FF69B4")

    point_v2 = intersection(trap2.v[0], trap2.v[1], Rules.rule_v[0], Rules.rule_v[1])
    plt.subplot(246)
    plt.plot(trap2.v[0], trap2.v[1], 'b', Rules.rule_v[0], Rules.rule_v[1], 'r')
    plt.scatter(point_v2[0], point_v2[1], color="#FF69B4")

    plt.subplot(247)
    trunc2 = Trapezoid([Rules.w_2, find_min_point(point_x2, point_v2)])
    trunc2.trapezoid()
    plt.plot(Rules.rule_w_2[0], Rules.rule_w_2[1], trunc2.lst_x, trunc2.lst_y, 'g')

    lst = []
    lst.append(trunc1)
    lst.append(trunc2)
    for i in lst:
        print(type(i))
    f = func(lst)
    f = area(f)
    plt.subplot(144)
    plt.plot(trunc1.lst_x, trunc1.lst_y, trunc2.lst_x, trunc2.lst_y)
    plt.xlabel('a center of mass ={}'.format(f))
    print('a center of mass =', f)

    print(making_rules(int(input())))
    plt.show()

    # trap = Trapezoid(list(map(float, input().split())))
    # trap2 = Trapezoid(list(map(float, input().split())))
    # trap.trapezoid()
    # trap2.trapezoid()
    # point = intersection(trap.lst_x, trap.lst_y, trap2.lst_x, trap2.lst_y)
    #
    # plt.subplot(131)
    # plt.plot(trap.lst_x, trap.lst_y, 'b', trap2.lst_x, trap2.lst_y, 'r')
    # plt.scatter(point[0], point[1], color="#7B68EE")
    #
    # plt.subplot(132)
    # # Передача q
    # trunc_default = Trapezoid([2, 1])
    # trunc = Trapezoid([4, point[1]])
    # trunc_default.trapezoid()
    # trunc.trapezoid()
    # plt.plot(trunc_default.lst_x, trunc_default.lst_y, trunc.lst_x, trunc.lst_y, 'r--')
    #
    # plt.subplot(133)
    # trunc1 = Trapezoid([1.5, 0.4])
    # trunc2 = Trapezoid([5, 1])
    # trunc3 = Trapezoid([3, 0.6])
    #
    # lst = []
    # lst.append(trunc1)
    # lst.append(trunc2)
    # lst.append(trunc3)
    # f = func(lst)
    # f = area(f)
    # print(f)
    # # print(find_not_zero(lst))
    #
    # trunc1.trapezoid()
    # trunc2.trapezoid()
    # trunc3.trapezoid()
    # plt.plot(trunc1.lst_x, trunc1.lst_y, 'r--')
    # plt.plot(trunc2.lst_x, trunc2.lst_y, 'b--')
    # plt.plot(trunc3.lst_x, trunc3.lst_y, 'g--')
    #
    # plt.show()
