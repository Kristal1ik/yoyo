from remade_functions import Controller, intersection, Rules, Trapezoid, find_min_point, func, area
import matplotlib.pyplot as plt

if __name__ == '__main__':
    trap1 = Controller([[6, 1], [8, 1]])
    trap2 = Controller([[7, 1], [2, 1]])
    trap3 = Controller([[8, 1], [4, 1]])
    trap4 = Controller([[5, 1], [6, 1]])
    trap5 = Controller([[2, 1], [5, 1]])

    point_x1 = intersection(trap1.x[0], trap1.x[1], Rules.rule_x[0], Rules.rule_x[1])
    point_x2 = intersection(trap2.x[0], trap2.x[1], Rules.rule_x[0], Rules.rule_x[1])
    point_x3 = intersection(trap3.x[0], trap3.x[1], Rules.rule_x[0], Rules.rule_x[1])
    point_x4 = intersection(trap4.x[0], trap4.x[1], Rules.rule_x[0], Rules.rule_x[1])
    point_x5 = intersection(trap5.x[0], trap5.x[1], Rules.rule_x[0], Rules.rule_x[1])

    point_v1 = intersection(trap1.v[0], trap1.v[1], Rules.rule_v[0], Rules.rule_v[1])
    point_v2 = intersection(trap2.v[0], trap2.v[1], Rules.rule_v[0], Rules.rule_v[1])
    point_v3 = intersection(trap3.v[0], trap3.v[1], Rules.rule_v[0], Rules.rule_v[1])
    point_v4 = intersection(trap4.v[0], trap4.v[1], Rules.rule_v[0], Rules.rule_v[1])
    point_v5 = intersection(trap5.v[0], trap5.v[1], Rules.rule_v[0], Rules.rule_v[1])

    trunc1 = Trapezoid([Rules.w_1, find_min_point(point_x1, point_v1)])
    trunc2 = Trapezoid([Rules.w_1, find_min_point(point_x2, point_v2)])
    trunc3 = Trapezoid([Rules.w_1, find_min_point(point_x3, point_v3)])
    trunc4 = Trapezoid([Rules.w_1, find_min_point(point_x4, point_v4)])
    trunc5 = Trapezoid([Rules.w_1, find_min_point(point_x5, point_v5)])

    trunc1.trapezoid()
    trunc2.trapezoid()
    trunc3.trapezoid()
    trunc4.trapezoid()
    trunc5.trapezoid()

    lst = []
    lst.append(trunc1)
    lst.append(trunc2)
    lst.append(trunc3)
    lst.append(trunc4)
    lst.append(trunc5)
    f = func(lst)
    f = area(f)
    plt.subplot()
    plt.plot(trunc1.lst_x, trunc1.lst_y, 'b', trunc2.lst_x, trunc2.lst_y, 'r',
             trunc3.lst_x, trunc3.lst_y, 'g', trunc4.lst_x, trunc4.lst_y,
             trunc5.lst_x, trunc5.lst_y, 'r')
    plt.scatter(f, 0, color="#7B68EE")
    plt.scatter(f, 1, color="#7B68EE", alpha=0)

    plt.xlabel('a center of mass ={}'.format(f))
    print('a center of mass =', f)

    plt.show()
