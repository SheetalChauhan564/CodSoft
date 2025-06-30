print("Simple Calculator ") 
a = int(input(" Enter the value of a= ")) 
b = int(input (" Enter the value of b= ")) 
choice = input (" Enter the '+' , '-', '*', '/', '%'= ") 

if choice == '+':
    result = a + b
    print("result", result)

elif choice == '-':
    result = a - b
    print("result", result)

elif choice == '*':
    result = a * b
    print("result", result)

elif choice == '/':
    if b != 0:
        result = a / b
        print("result", result)
    else:
        print("Error: Division by zero")

elif choice == '%':
    if b != 0:
        result = a % b
        print("result", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")