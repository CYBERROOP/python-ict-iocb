def f(x, y):
    return x + y  # Example ODE: dy/dx = x + y

def modified_euler(x0, y0, x_end, h):
    x = x0
    y = y0
    iterations = 0

    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += (h / 2) * (k1 + k2)
        x += h
        iterations += 1

    print(f"Final y is : {y:.4f}")
    print(f"Number of iterations: {iterations}")

# Inputs
x0 = 0
y0 = 1
x_end = 1
h = 0.1

modified_euler(x0, y0, x_end, h)
