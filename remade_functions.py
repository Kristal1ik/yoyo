import matplotlib.pyplot as plt


class Trapezoid:
    def __init__(self, params):
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
    trap = Trapezoid(list(map(float, input().split())))
    trap2 = Trapezoid(list(map(float, input().split())))
    trap.trapezoid()
    trap2.trapezoid()
    point = intersection(trap.lst_x, trap.lst_y, trap2.lst_x, trap2.lst_y)

    plt.subplot(131)
    plt.plot(trap.lst_x, trap.lst_y, 'b', trap2.lst_x, trap2.lst_y, 'r')
    plt.scatter(point[0], point[1], color="#7B68EE")

    plt.subplot(132)
    # Передача q
    trunc_default = Trapezoid([1.0, 3.0, 6.0, 7.0, 1.0])
    trunc = Trapezoid([1.0, 3.0, 6.0, 7.0, point[1]])
    trunc_default.trapezoid()
    trunc.trapezoid()
    plt.plot(trunc_default.lst_x, trunc_default.lst_y, trunc.lst_x, trunc.lst_y, 'r--')

    plt.subplot(133)
    trunc1 = Trapezoid([0.1, 0.2, 3.0, 5.8, 0.4])
    trunc2 = Trapezoid([1.0, 4.0, 5.5, 9.0, 1])
    trunc3 = Trapezoid([0.5, 2.0, 3.5, 7.0, 0.6])

    lst = []
    lst.append(trunc1)
    lst.append(trunc2)
    lst.append(trunc3)
    f = func(lst)
    f = area(f)
    print(f)
    # print(find_not_zero(lst))

    trunc1.trapezoid()
    trunc2.trapezoid()
    trunc3.trapezoid()
    plt.plot(trunc1.lst_x, trunc1.lst_y, 'r--')
    plt.plot(trunc2.lst_x, trunc2.lst_y, 'b--')
    plt.plot(trunc3.lst_x, trunc3.lst_y, 'g--')

    plt.show()
# y = kx + b
# k = (y - b) / x
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k*x2
