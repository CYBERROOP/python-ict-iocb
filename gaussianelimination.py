# Define the augmented matrix [A|b]
# Coefficients of u, y, z in each equation
A = [
    [1, -3, 2],   # Row 0      #x-3y+2z=5
    [-2, 3, -5],  # Row 1  #for 2x2 upto this line    #-2x+3y-5z=6
    [4, -1, 3]    # Row 2 (new equation) #for 3x3     #4x-y+3z=7
]
# Constants on the right-hand side of the equations

# b = [5, 6]#for 2x2

b = [5, 6, 7]#for3x3

# Forward Elimination Step (Gaussian Elimination)
def forward(A, b):
    n = len(b)  #output : 2  
    for i in range(n):  # Iterate over each column
     max = i  # Assume the current row has the largest pivot
    for j in range(i+1, n):  # Check rows below the current row
        if abs(A[j][i]) > abs(A[max][i]):  # Compare absolute values
            max = j  # Update max to the row with the largest pivot

# first it took 1row as max in i then it checks i+1 in j 
# now if it find a row then it updates the j as 2row as max 
# now new max is 2 and it runs so on
        
        # Swap rows
        A[i], A[max] = A[max], A[i]
        b[i], b[max] = b[max], b[i]

# question : A = [
#     [1, -3, 2],  # Row 0
#     [-2, 3, -5]  # Row 1
# ]
# b = [5, 6]

# concept : A[0], A[1] = A[1], A[0]
# b[0], b[1] = b[1], b[0]

# output : A = [
#     [-2, 3, -5],  # Row 1 becomes row 0
#     [1, -3, 2]    # Row 0 becomes row 1
# ]
# b = [6, 5]

        # Eliminate column below pivot
    for j in range(i+1, n):  # Iterate over rows below the current row
        if A[j][i] != 0:  # Check if the element below the pivot is non-zero
            factor = A[j][i] / A[i][i]  # Compute the factor to eliminate the element
            for k in range(i, n):  # Iterate over columns in the row
                A[j][k] -= factor * A[i][k]  # Subtract the scaled pivot row from the current row
            b[j] -= factor * b[i]  # Update the corresponding element in vector b
    return A, b
# input after above pivot : A = [
#     [-2, 3, -5],  # Row 0
#     [1, -3, 2]    # Row 1
# ]
# b = [6, 5]

# method : A[0][0] = -2
# A[1][0] = 1 => factor A[1][0]/A[0][0] = factor (1/-2) = -0.5
# now update row1 :
# A[1][0] = 1-(-0.5) = 1.5
# Subtract this value from ( A[1][1] ): [ A[1][1] = -3 - (-1.5) = -3 + 1.5 = -1.5 ]
# OUTPUT : A = [
#     [-2, 3, -5],   # Row 0 (unchanged)
#     [0, -1.5, 2]   # Row 1 (updated)
# ]


# Back Substitution Step (Solving the system)
def back(A, b):
    n = len(b)
    x = [0] * n
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]
    return x

#reverse back substitution for varification of forward substitution

# Solve the system using Gaussian Elimination
A, b = forward(A, b)
solution = back(A, b)

# Extract the values of u, y, z

# x,y = solution   #for 2x2

x,y,z = solution  #for 3x3

# Print the result
print(f"u = {x:.2f}, y = {y:.2f},z = {z:.2f}")
print(f"root of all equations = ±√u = ±{x**0.5:.2f}")

