print("Hello, Please Use Our Calculator")
print("You can perform simple Arithmetic Calculations here.")
#I have included this line, so that user feel comfortable to use this

# Accepting user input, which I have set the data type as 'Float' so that both integer and decimal numbers gets accepted
x = float(input("Please Enter a Number: "))
y = float(input("Please Enter another Number: "))

# Asking the user what operation they want to perform
print("Please mention what Arithmetic Calculation You want to pursue:")
print("To ADD the Numbers, type '+'")
print("To SUBTRACT the Numbers, type '-'")
print("To MULTIPLY the Numbers, type '*'")
print("To DIVIDE the Numbers, type '/'")

operation = input("Please, Enter your choice: ")

# Perform the selected operation
if operation == "+":
    print(f"The result of addition is: {x + y}")
elif operation == "-":
    print(f"The result of subtraction is: {x - y}")
elif operation == "*":
    print(f"The result of multiplication is: {x * y}")
elif operation == "/":
    if y != 0:
        print(f"The result of division is: {x / y}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please choose 'add', 'minus', 'into', or 'by'.")

print("Thank You, for Using Our Calculator") 