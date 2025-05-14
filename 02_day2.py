# CONTAINER TYPE : 1.LIST  2. TUPPLES 3. SETS  4. DICTIONARY

print(bin(10))

x = 12.023 #floting number 
#converting float -> int 
print(int(x))
x=20
#convert it to complex number 
print(complex(x)) 
#convert to octal 
print(oct(x))
#convert to hex
print(hex(x))

#
a = [10,20,30]

print(a[:3])
a.insert(2,"dexter")
print(a)

a.remove(10)
print(a)

a = "dexter \n"
b = "sampreet"

p = '''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!'''

print(p)


letter="Dexter is  a good boy  "
print(letter.find("  "))

p = "dexter is a good boy"
print (p.isupper())
print(p.islower())
p = "20"           #all is functions are workable inside quotes
print(p.isdigit())
print(p.isprintable())
print(p.startswith("2"))


a= "Bombay"
b= "bombay"

print(a==b)

#TEXT TO BINARY NUMBER   (NOT IN SYLLABUS)
# a = "Bombay"
# binary_output = ' '.join(format(ord(char), '08b') for char in a)
# print(binary_output)

# a = "bombay"
# binary_output = ' '.join(format(ord(char), '08b') for char in a)
# print(binary_output)
