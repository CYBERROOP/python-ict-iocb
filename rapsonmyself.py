def f(x):
    return x**3 - x - 2  # Finding the roots of x^3 - x - 2

def df(x):
    return 3*x**2 - 1  # Derivative of f(x)

def newtonsrapsonmethod(x0, tol=0.00001, max_iter=100):

    if df(x0) == 0 : 
        print("method fails ")
    else : 
        i = 0  # Initialize iteration counter
        while True:  # Limit the number of iterations when it is true 
            x1 = x0 - f(x0) / df(x0)  # Newton-Raphson formula
            if abs(x1 - x0) < tol:  # Check for convergence
             break  # breaking the root and iteration count
            x0 = x1  # Update x0 for the next iteration
            i += 1  # Increment iteration counter
        
        return x1, i  # Return None if no solution is found

# Initial guess
x0 = 1
root, iterations = newtonsrapsonmethod(x0)

if root is not None:
    print(f"{root} is the root of the equation")
    print(f"{iterations} iterations were required to find the root")
else:
    print("No root found within the maximum number of iterations")


 



