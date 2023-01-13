def perform_operation(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

operator = input("Enter operator (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(perform_operation(operator, num1, num2))
