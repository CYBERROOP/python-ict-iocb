def gcd(a, b):
    while b:  # Loop until b becomes 0
        a, b = b, a % b  # Swap values and take remainder
    return a  # When b is 0, a is the GCD

m = int(input("num 1 is : "))
n = int(input("num 2 is : "))
print(gcd(m,n))


# import math

# # m = int(input("num 1 : "))
# # n = int(input("num 2 : "))
# # p = math.gcd(m,n)
# # print(p)
# print(math.gcd(12,16))




