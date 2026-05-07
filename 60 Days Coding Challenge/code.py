num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operator = input("Enter operator (+, -, *, /):")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif num2==0 and operator =="/":
    print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")