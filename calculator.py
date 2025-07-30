print("Basic Calculator Program")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(num1, "+", num2, "=", float(num1) + float(num2))
elif op == "-":
    print(num1, "-", num2, "=", float(num1) - float(num2))
elif op == "*":
    print(num1, "*", num2, "=", float(num1) * float(num2))
elif op == "/":
    if float(num2) == 0:
        print("Error: Division by zero")
    else:
        print(num1, "/", num2, "=", float(num1) / float(num2))
else:
    print("Invalid operation")
