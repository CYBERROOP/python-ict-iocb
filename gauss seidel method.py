# Gauss-Seidel Method in Python

def gauss_seidel(a, b, x0, tolerance, max_iterations):  #ax = b method where a defines matrix 
    n = len(a)  # size of matrix how number of row make in length
    x = x0[:]  #here x = [0 0 0] value of x0 initially
    for iteration in range(max_iterations):
        x_new = x[:]  # old x value new x value se exchange hogaya

        for i in range(n):
            sum1 = sum(a[i][j] * x_new[j] for j in range(i)) #it updates the x_new value of lower triangular matrix
            sum2 = sum(a[i][j] * x[j] for j in range(i + 1, n)) #it updates the x_new value of upper triangular
            x_new[i] = (b[i] - sum1 - sum2) / a[i][i]

            # uses the Gauss-Seidel method to iteratively solve a linear system
            # by improving estimates of x until the solution converges.
        
        # Check for convergence
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):  #checking the iteration acc to tolerance 
            return x_new, iteration + 1
        
        x = x_new  #after getting new x_new value which pushed in to X
    return x, max_iterations

# Example usage
a = [
    [7, 1, 2],  #7x+y+2z = 4
    [3, 5, 1],   #3x+5y+z = 7
    [1, 1, 3]    #x+y+3z = 3
]
b = [4, 7, 3]
x0 = [0, 0, 0]  # Initial guess
tolerance = 0.0001
max_iterations = 100

solution, iterations = gauss_seidel(a, b, x0, tolerance, max_iterations)
print("\n")
print("Solution:", solution )
print("Iterations:", iterations)
print("\n")