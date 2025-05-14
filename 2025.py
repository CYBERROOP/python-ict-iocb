# find the roots of x^3-1 = 0 

def f(x):
    return x**3 - 1

def bisection(a, b, tol=0.0001, max_iter=100):  #tolerance (tol) is FSILEN , max_iteration = 100 to prevent infinite loops
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        
        if abs(f(c)) < tol:   #HERE ABS is absolute value (mod value)
            return c
        
        if f(c) * f(a) <= 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

# Find the real root using bisection method
root = bisection(1, 2)
print(f"Real root using bisection method: {root:.4f}")





# import numpy as np 
# coeff = [1,0,0,-1]
# roots = np.roots(coeff)
# print(f"roots = " ,roots)