import math

from remade_functions_numpy import Controller, intersection, Trapezoid, \
    find_min_point, func, area, Rules
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    y = lambda x: np.sin(x)
    # создаём рисунок с координатную плоскость
    fig = plt.subplots()
    # создаём область, в которой будет
    # - отображаться график
    x = np.linspace(-3, 3, 100)
    # значения x, которые будут отображены
    # количество элементов в созданном массиве
    # - качество прорисовки графика
    # рисуем график
    plt.plot(x, y(x))
    # показываем график

    # show the plot
    # trap = Controller([[6, 1], [4, 1]])
    # point_x = intersection(trap.x[0], trap.x[1], Rules.rule_x[0], Rules.rule_x[1])
    #
    #
    # point_v = intersection(trap.v[0], trap.v[1], Rules.rule_v[0], Rules.rule_v[1])
    #
    # trunc1 = Trapezoid([Rules.w1, find_min_point(point_x, point_v)])
    # trunc1.trapezoid()
    #
    #
    # trap2 = Controller([[2, 1], [6, 1]])
    #
    # point_x2 = intersection(trap2.x[0], trap2.x[1], Rules.rule_x[0], Rules.rule_x[1])
    #
    # point_v2 = intersection(trap2.v[0], trap2.v[1], Rules.rule_v[0], Rules.rule_v[1])
    #
    # trunc2 = Trapezoid([Rules.w2, find_min_point(point_x2, point_v2)])
    # trunc2.trapezoid()
    # lst = []
    # lst.append(trunc1)
    # lst.append(trunc2)
    # f = func(lst)
    # lst_x = []
    # shag = 0.01
    # for i in range(1000):
    #     lst_x.append(shag)
    #     shag += 0.01
    # plt.subplot()
    # print(f)
    # f = area(f)
    # plt.plot(trunc1.lst_x, trunc1.lst_y, 'g', trunc2.lst_x, trunc2.lst_y, 'g')
    # plt.scatter(f, 0, color="#7B68EE")
    # plt.scatter(f, 1, color="#7B68EE", alpha=0)
    #
    # plt.xlabel('a center of mass ={}'.format(f))
    # print('a center of mass =', f)
    #
    # print(making_rules(int(input())))
    plt.show()