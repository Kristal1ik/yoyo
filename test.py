def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    print(f(b), b, a, f(a))
    s += f(b)/2.0
    return s * h

print( trapezoidal(lambda x:x**2, 5, 10, 100))