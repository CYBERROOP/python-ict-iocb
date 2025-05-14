s = "BHUBANESWAR - 751013"
alphabet = numbers = spec_char = 0  # Initialize all counters

for i in range(len(s)):  # Use the correct variable name
    if s[i].isalpha():
        alphabet += 1
    elif s[i].isdigit():
        numbers += 1  # Corrected variable name
    else:
        spec_char += 1

print("Alphabets:", alphabet)
print("Digits:", numbers)
print("Special Characters:", spec_char)








str = "BHUBANESWAR - 751013"
alphabet = digits = spec_char = 0 
for i in range (len(str)):
    if str[i].isalpha():
        alphabet += 1
    elif str[i].isdigit():
        digits  = digits + 1
    else :
        spec_char+=1
print("alphabets are : ",alphabet)
print("digits : ",digits)
print("special character : ", spec_char)