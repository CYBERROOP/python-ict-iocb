def f(x):
    return x**3 - x - 2  # example function

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Divide by zero error in iteration", i)
            return None
        
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        
        if abs(x2 - x1) < tol:
            print(f"Root found at x = {x2} after {i+1} iterations")
            return x2
        
        x0, x1 = x1, x2

    print("Max iterations reached without convergence")
    return None

# Example usage
root = secant_method(f, 2,9)
