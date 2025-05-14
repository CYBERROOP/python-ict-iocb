def f(x):
    return x**3 - x - 2

def bisection(a, b):
    while abs(b - a) > 0.0001:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("Root =", c)

bisection(1, 2)