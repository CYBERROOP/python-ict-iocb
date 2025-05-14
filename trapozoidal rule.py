def f(x):
    return 1/x 
def trapozoidal ( x0 , xn , n ) : 
    h = (x0- xn) /n
    location = f(x0) + f(xn)
    for i in range (1,n) : 
        xi = x0 + i * h 
        location = location + 2 * f(xi)
    location = h / 2 * location 
    return location
print(trapozoidal(4,6,6))

        



