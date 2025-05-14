# while condition : 
#     print("comment")

# n = 0 
# sum = 0 
# while (n <= 100 ) : 
#     sum = sum + n 
#     n += 1
#     print(sum)

# i = 1
# while (i <= 100) : 
#     print(i , end = ",")
    
#     i = i+1
import time

try:
    n = int(input("ENTER HOW MANY NUMBERS YOU WANT TO PRINT: "))
    print("printing numbers:")
    time.sleep(1)
    i = n
    while i > 0:
        print(i, ";", end=" ")  # Use end=" " to print on the same line
        i += 1
    print() #print a newline at the end.
except ValueError:
    print("Invalid input. Please enter a number.")