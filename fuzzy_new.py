class Trapezoid:
    def __init__(self, params):
        if len(params) == 2:
            n = params[0]
            self.a = n - 2
            self.b = n - 1
            self.c = n + 1
            self.d = n + 2
            self.h = params[1]
        elif len(params) == 5:
            self.a = params[0]
            self.b = params[1]
            self.c = params[2]
            self.d = params[3]
            self.h = params[4]
        self.lst_y = []
        self.lst_x = []
        self.lst_h = []