from remade_functions import Controller, intersection, Rules, Trapezoid, \
    find_min_point, func, area, making_rules
import matplotlib.pyplot as plt

if __name__ == '__main__':
    trap = Controller([[6, 1], [8, 1]])
    point_x = intersection(trap.x[0], trap.x[1], Rules.rule_x[0], Rules.rule_x[1])
    plt.subplot(331)
    plt.plot(trap.x[0], trap.x[1], 'b', Rules.rule_x[0], Rules.rule_x[1], 'r')
    plt.scatter(point_x[0], point_x[1], color="#7B68EE")

    point_v = intersection(trap.v[0], trap.v[1], Rules.rule_v[0], Rules.rule_v[1])
    plt.subplot(332)
    plt.plot(trap.v[0], trap.v[1], 'b', Rules.rule_v[0], Rules.rule_v[1], 'r')
    plt.scatter(point_v[0], point_v[1], color="#7B68EE")

    plt.subplot(333)
    trunc1 = Trapezoid([Rules.w_1, find_min_point(point_x, point_v)])
    trunc1.trapezoid()
    plt.plot(Rules.rule_w[0], trunc1.lst_y, 'g', Rules.rule_w[0], Rules.rule_w[1])

    trap2 = Controller([[3, 1], [6, 1]])

    point_x2 = intersection(trap2.x[0], trap2.x[1], Rules.rule_x[0], Rules.rule_x[1])
    plt.subplot(334)
    plt.plot(trap2.x[0], trap2.x[1], 'b', Rules.rule_x[0], Rules.rule_x[1], 'r')
    plt.scatter(point_x2[0], point_x2[1], color="#FF69B4")

    point_v2 = intersection(trap2.v[0], trap2.v[1], Rules.rule_v[0], Rules.rule_v[1])
    plt.subplot(335)
    plt.plot(trap2.v[0], trap2.v[1], 'b', Rules.rule_v[0], Rules.rule_v[1], 'r')
    plt.scatter(point_v2[0], point_v2[1], color="#FF69B4")

    plt.subplot(336)
    trunc2 = Trapezoid([Rules.w_2, find_min_point(point_x2, point_v2)])
    trunc2.trapezoid()
    plt.plot(Rules.rule_w_2[0], Rules.rule_w_2[1], trunc2.lst_x, trunc2.lst_y, 'g')

    plt.subplot(337)
    plt.scatter(0, 1, color="#7B68EE", alpha=0)
    plt.plot(Rules.rule_w[0], trunc1.lst_y, 'g')

    plt.subplot(338)
    plt.scatter(0, 1, color="#7B68EE", alpha=0)
    plt.plot(trunc2.lst_x, trunc2.lst_y, 'g')

    lst = []
    lst.append(trunc1)
    lst.append(trunc2)
    f = func(lst)

    f = area(f)
    plt.subplot(339)
    plt.plot(trunc1.lst_x, trunc1.lst_y, 'b', trunc2.lst_x, trunc2.lst_y, 'r')
    plt.scatter(f, 0, color="#7B68EE")
    plt.scatter(f, 1, color="#7B68EE", alpha=0)

    plt.xlabel('a center of mass ={}'.format(f))
    print('a center of mass =', f)

    print(making_rules(int(input())))
    plt.show()
