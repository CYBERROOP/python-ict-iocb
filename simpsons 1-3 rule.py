def f(x) : 
    return 1/x 
def simpsons(x0 , xn , n ) : 
    h = (x0-xn)/n
    location = f(x0)+f(xn)
    for i in range ( 1, n ) : 
        xi = x0 + i * h 
        if i % 2 == 0 : 
            location = location + 2 * f(xi)
        else : 
            location = location  + 4*f(xi)
    area = (h/3) * location
    return area 
print(simpsons(16,6,6))
