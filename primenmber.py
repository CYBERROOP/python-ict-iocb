# PRIME NUMBER FROM 0 TO 300 

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

print("Prime numbers between 0 and 300:")
for num in range(300):  # Loop from 0 to 300
    if prime(num):
        print(num, end=";")
