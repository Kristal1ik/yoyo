from remade_functions import Controller, Rules_consts, intersection, rules, Trapezoid, find_min_point, func, area
import matplotlib.pyplot as plt

if __name__ == '__main__':

    trap1 = [Controller([[6, 1], [8, 1]]),
             Controller([[7, 1], [2, 1]]),
             Controller([[8, 1], [4, 1]]),
             Controller([[5, 1], [6, 1]]),
             Controller([[2, 1], [5, 1]])]
    n = int(input())
    rules = rules(n)
    lst = []
    print(rules[0][0])
    print(len(trap1))
    for i in range(n):
        point_x = intersection(trap1[i].x[0], trap1[i].x[1], rules[i][0][0], rules[i][0][1])
        point_v = intersection(trap1[i].v[0], trap1[i].v[1], rules[i][1][0], rules[i][1][1])
        trunc = Trapezoid([Rules_consts.w, find_min_point(point_x, point_v)])
        trunc.trapezoid()
        lst.append(trunc)
        plt.plot(trunc.lst_x, trunc.lst_y, 'b')
    f = func(lst)
    lst_x = []
    shag = 0.01
    for i in range(1000):
        lst_x.append(shag)
        shag += 0.01
    plt.subplot()
    print(f)
    plt.plot(lst_x, f)

    f = area(f)
    print(lst[0])

    plt.scatter(f, 0, color="#7B68EE")
    plt.scatter(f, 1, color="#7B68EE", alpha=0)

    plt.xlabel('a center of mass ={}'.format(f))
    print('a center of mass =', f)

    plt.show()
