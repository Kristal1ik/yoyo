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
    print(lst_intersection)
    print(max_y)
    return max_y[::-1]


class Controller:
    def __init__(self, params):
        self.x = Trapezoid(params[0]).trapezoid()
        self.v = Trapezoid(params[1]).trapezoid()
        self.w = Trapezoid(params[2]).trapezoid()


class Rulers:
    rule_x = Trapezoid([5, 1]).trapezoid()
    rule_v = Trapezoid([5, 1]).trapezoid()
    rule_w = Trapezoid([5, 1]).trapezoid()


# def find_not_zero(lst_m):


#     min_a = 2
#     max_d = -0.5
#     for i in lst_m:
#         if i.a < min_a:
#             min_a = i.a
#         if i.d > max_d:
#             max_d = i.d
#     return min_a, max_d


if __name__ == '__main__':
    trap = Controller([[3, 1], [7, 0.7], [6, 0.8]])

    point_x = intersection(trap.x[0], trap.x[1], Rulers.rule_x[0], Rulers.rule_x[1])
    plt.subplot(141)
    plt.plot(trap.x[0], trap.x[1], 'b', Rulers.rule_x[0], Rulers.rule_x[1], 'r')
    plt.scatter(point_x[0], point_x[1], color="#7B68EE")

    point_v = intersection(trap.v[0], trap.v[1], Rulers.rule_v[0], Rulers.rule_v[1])
    plt.subplot(142)
    plt.plot(trap.v[0], trap.v[1], 'b', Rulers.rule_v[0], Rulers.rule_v[1], 'r')
    plt.scatter(point_v[0], point_v[1], color="#7B68EE")

    point_w = intersection(trap.w[0], trap.w[1], Rulers.rule_w[0], Rulers.rule_w[1])
    plt.subplot(143)
    plt.plot(trap.w[0], trap.w[1], 'b', Rulers.rule_w[0], Rulers.rule_w[1], 'r')
    plt.scatter(point_w[0], point_w[1], color="#7B68EE")

    plt.subplot(144)
    q_x = Trapezoid([3, point_x[1]])
    q_x.trapezoid()
    q_v = Trapezoid([7, point_v[1]])
    q_v.trapezoid()
    q_w = Trapezoid([6, point_w[1]])
    q_w.trapezoid()
    plt.plot(q_x.lst_x, q_x.lst_y, 'y', q_v.lst_x, q_v.lst_y, 'b', q_w.lst_x, q_w.lst_y, 'g')

    lst = []
    lst.append(q_x)
    lst.append(q_v)
    lst.append(q_w)
    f = func(lst)
    f = area(f)
    plt.xlabel('a center of mass ={}'.format(f))

    print('a center of mass =', f)
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
