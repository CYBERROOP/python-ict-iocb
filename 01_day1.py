import keyword
import math

print(keyword.kwlist)   #list of keywords printing

a = 10
b = 20

c = a + b
print(c)

print(type(a))  #int type

print(type(b))  #int type

z = 1+1j
print(type(z))  #complex type

name = "Python"
print(type(name))  #string type

list = [1, 2, 3, 4, 5]
print(type(list))   #list type

d =True
print(type(d))  #bool type

dict = (1, 2, 3, 4, 5)
print(type(dict))   #tuple type

DISK = {1, 2, 3, 4, 5}
print(type(DISK))   #set type

dictionary = {1: 'one', 2: 'two', 3: 'three' , "no of elements":3}
print(type(dictionary))   #dictionary type


print(math.pi) #value of pi
a = math.sin((90))
print((a))

print(math.sqrt(25))  #square root of 25

print(math.sin(math.pi /2))

print(dir(math))  #list of functions in math module

a = 10
b = 20
c = 30
print(a+b)
print(a-b)
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a!=b)
print(a&b)

print(all((a<b,b>c)))
print(any((a<b,b>c)))