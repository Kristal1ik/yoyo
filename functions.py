import matplotlib.pyplot as plt


# y = kx + b
# k = (y - b) / x
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k*x2

# Треугольная
def triangle(tria):
    global y
    lst_y = []
    lst_x = []
    a, b, c = tria[0], tria[1], tria[2]
    f1 = False
    f2 = False
    x1, x2, y1, y2, xx1, xx2, yy1, yy2 = 0, 0, 0, 0, 0, 0, 0, 0
    for x in range(-10, 10):
        lst_x.append(x)
        if x <= a:
            y = 0
            if not f1 and x == a:
                x1 = x
                y1 = y
                f1 = True
        elif (x >= a) and (x <= b):
            y = (x - a) / (b - a)
            if y == 1:
                x2 = x
                y2 = y
        elif (x >= b) and (x < c):
            y = (c - x) / (c - b)
            if not f2:
                xx1 = x
                yy1 = y
                f2 = True
        elif x >= c:
            y = 0
            if x == c:
                xx2 = x
                yy2 = y
        lst_y.append(y)
    print(lst_x, lst_y)
    print(x1, y1, x2, y2, xx1, yy1, xx2, yy2)
    # the first line
    print('the first line')
    print("k={}".format((y1 - y2) / (x1 - x2)))
    print("b={}".format(y2 - ((y1 - y2) / (x1 - x2)) * x2))
    # the second line
    print('the second line')
    print("k={}".format((yy1 - yy2) / (xx1 - xx2)))
    print("b={}".format(yy2 - ((yy1 - yy2) / (xx1 - xx2)) * xx2))
    return lst_x, lst_y
    # plt.plot(lst_x, lst_y)
    # plt.ylabel('triangle')
    # plt.show()


# Трапецеидальная
def trapezoid(trap):
    global y
    lst_y = []
    lst_x = []
    lst_h = []
    a, b, c, d, h = trap[0], trap[1], trap[2], trap[3], None
    x = 0.01
    if len(trap) > 4:
        h = trap[4]
    for i in range(1000):
        lst_x.append(float(x))
        if (x >= a) and (x <= b):
            y = 1 - ((b - x) / (b - a))
        elif (x >= b) and (x <= c):
            y = 1
        elif (x >= c) and (x <= d):
            y = 1 - ((x - c) / (d - c))
        else:
            y = 0
        x += 0.01
        if h is not None:
            if float(y) >= h:
                lst_h.append(h)
            elif float(y) < h:
                lst_h.append(y)
            else:
                h = 0
                lst_h.append(h)
        lst_y.append(float(y))
    if not None:
        lst_y = lst_h
    return lst_x, lst_y


# Нахождение точки пересечения (y, x)
def intersection(one, two, a1, d2):
    one_x = one[0]
    one_y = one[1]
    two_x = two[0]
    two_y = two[1]
    lst_intersection = []
    x = 0.01
    for i in range(1000):
        if round(one_y[i], 2) == round(two_y[i], 2) and one_y[i] != 0 and two_y != 0:
            lst_intersection.append([one_y[i], one_x[i]])
        x += 0.01
    max_y = max(lst_intersection)
    print(lst_intersection)
    print(max_y)
    return max_y


def area(mn_a, mx_d, ):
    ...


if __name__ == '__main__':
    one = list(map(float, input().split()))
    two = list(map(float, input().split()))
    one_trap = trapezoid(one)
    two_trap = trapezoid(two)
    point = (intersection(one_trap, two_trap, one[0], two[-1]))

    plt.subplot(131)
    plt.plot(one_trap[0], one_trap[1], 'b', two_trap[0], two_trap[1], 'r')
    plt.scatter(point[1], point[0], color="#7B68EE")

    plt.subplot(132)
    # Передача q
    trunc = trapezoid([1.0, 3.0, 4.0, 6.0, point[0]])
    plt.plot(trunc[0], trunc[1])
    plt.plot(trunc[0], trunc[-1], 'r--')

    plt.subplot(133)
    trunc = trapezoid([1.0, 3.0, 4.0, 6.0, point[0]])
    trunc2 = trapezoid([1.0, 4.0, 5.5, 9.0, 1])
    trunc3 = trapezoid([0.5, 2.0, 3.5, 7.0, 0.6])
    # plt.plot(trunc[0], trunc[1])
    plt.plot(trunc[0], trunc[-1], 'r--')
    plt.plot(trunc2[0], trunc2[-1], 'b--')
    plt.plot(trunc3[0], trunc3[-1], 'g--')



    plt.show()
