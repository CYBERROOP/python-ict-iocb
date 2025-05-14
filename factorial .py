# import math

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {math.factorial(num)}\n")
# #print("FACTORIAL OF " ,num , "is : " , math.factorial(num))


def fact(m):
    num = 1
    for i in range(1, m + 1):
        num = num* i
    print(num)

l = int(input("Enter number: "))
fact(l)

