import random


class Const:
    dna_length = 14


def f(x):
    # Качество бинарной строчки
    return -((x - 9) ** 2)


# def find_best(lst):
#     mx = ''
#     for i in lst:
#         if i.dna.count("1") > mx.count("1"):
#             mx = i.dna
#     return mx


class Individ:
    def __init__(self):
        self.dna = ''
        for _ in range(Const.dna_length):
            self.dna += str(random.randint(0, 1))
        self.ab = [-20, 20]

    # Поиск пригодности (кол-во единиц)
    def fitness(self):
        # one_count = self.dna.count("1")
        # return one_count
        # Результат функции в данном индивиде
        y = f(self.ab[0] + ((self.ab[1] - self.ab[0]) * (int(self.dna, 2) / (2 ** Const.dna_length - 1))))
        return y

    # Выбор наилучшего из двух
    def best(self, other):
        if self.fitness() > other.fitness():
            return self
        # Глобальный минимум
        # if self.fitness() < other.fitness():
        #     return self
        return other

    # Скрещивание
    def crossing_over(self, other):
        ind1 = random.randint(0, Const.dna_length - 1)
        one_part = self.dna[:ind1]
        two_part = other.dna[ind1:]
        temp = Individ()
        temp.dna = ''.join(one_part + two_part)
        return temp

    # Мутация (замена случайного элемента)
    def mutation(self):
        for i in range(len(self.dna)):
            ind1 = random.random()
            if ind1 < 0.02:
                if self.dna[i] == "0":
                    # self.dna = self.dna[:ind1] + "0" + self.dna[ind1 + 1:]
                    self.dna = self.dna[:i] + "1" + self.dna[i + 1:]
                else:
                    # self.dna = self.dna[:ind1] + "1" + self.dna[ind1 + 1:]
                    self.dna = self.dna[:i] + "0" + self.dna[i + 1:]


if __name__ == '__main__':
    ind_lst = []
    new_generation_lst = []
    the_best_of_the_best = Individ()

    # all_people = []
    # Количество индивидов
    for i in range(20):
        ind_lst.append(Individ())
        if ind_lst[i].fitness() > the_best_of_the_best.fitness():
            the_best_of_the_best = ind_lst[i]

    # Количество поколений
    for i in range(1000):

        for j in range(20):
            mum1 = random.choice(ind_lst)
            mum_final = mum1.best(random.choice(ind_lst))

            dad1 = random.choice(ind_lst)
            dad_final = mum1.best(random.choice(ind_lst))

            child = mum_final.crossing_over(dad_final)
            child.mutation()

            new_generation_lst.append(child)
        ind_lst = new_generation_lst
        for i in range(len(ind_lst)):
            if ind_lst[i].fitness() > the_best_of_the_best.fitness():
                the_best_of_the_best = ind_lst[i]
        new_generation_lst = []

    mx = -1
    mx_hex = -1
    mx_mx = ''
    for i in ind_lst:
        print(i.ab[0] + ((i.ab[1] - i.ab[0]) * (int(i.dna, 2) / (2 ** Const.dna_length - 1))),
              f(i.ab[0] + ((i.ab[1] - i.ab[0]) * (int(i.dna, 2) / (2 ** Const.dna_length - 1)))))
        # print(i.dna)
    print("The best individ is", the_best_of_the_best.ab[0] + ((the_best_of_the_best.ab[1] - the_best_of_the_best.ab[0]) * (int(the_best_of_the_best.dna, 2) / (2 ** Const.dna_length - 1))),
              f(the_best_of_the_best.ab[0] + ((the_best_of_the_best.ab[1] - the_best_of_the_best.ab[0]) * (int(the_best_of_the_best.dna, 2) / (2 ** Const.dna_length - 1)))))
