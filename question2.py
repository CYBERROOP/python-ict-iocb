# suppose there are four flag variable a,b,c,d 
# write the program to check in multiple ways whether is it true ? 


a = 1  
b = 0 
c = 1 
d = 0 

if a or b or c or d : 
    print(f"one of them are TRUE  ")
else : 
    print("all false")

if any ((a,b,c,d)) : 
    print("one is true ")
else:
    print("all are false")

if 1 in (a,b,c,d):
    print(f"{1} is available its true")
else: 
    print("nothing available")