def f(x, y):
    return x + y  

def euler(x0, y0, x_end, h):
    x = x0
    y = y0
    iterations = 0
    while x < x_end:
        y = y + h * f(x, y)
        x = x+ h
        iterations = iterations + 1
    print(f"Final y is: {y:.4f}")
    print(f"Number of iterations: {iterations}")

# Inputs
x0 = 0
y0 = 1
x_end = 1
h = 0.1

euler(x0, y0, x_end, h)
