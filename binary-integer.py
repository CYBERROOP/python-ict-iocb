#binary to integer

binary_input = input("Enter a binary number: ")  # User enters a binary string
integer_value = int(binary_input, 2)  # Convert binary to integer
print(f"Integer value: {integer_value}")


#integer to binary

num = int(input("Enter an integer: "))
binary = format(num, 'b')
print("Binary:", binary)   
