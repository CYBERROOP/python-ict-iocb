def jacobi(a, b, n, x0, iterations): 
    for k in range(iterations) : 
        xnew = x0
        for i in range (n) : 
            sumi = 0 
            for j in range (n) : 
                if i!=j : 
                    sumi = sumi + a[i][j] * x0[i]
            xnew[i] = (b[i] - sumi )  / a[i][i]
        x0 = xnew
    return x0

# Inputs
x0 = [0, 0, 0]
n = 3 
a = [
    [4, 0, -1],
    [3, -1, 0],
    [4, 2, -3]
]
b = [9, 6, 8]
iterations = 100 

# Run
result = jacobi(a, b, n, x0, iterations)
print(result)
