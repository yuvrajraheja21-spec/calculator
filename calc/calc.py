# calculator

perform = ["+", "-", "*", "/", "**", "%"]
def calculator(a, b, operation):
    if operation == perform[0]:
        return a + b
    elif operation == perform[1]:
        return a - b
    elif operation == perform[2]:
        return a * b
    elif operation == perform[3]:
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == perform[4]:
        return a ** b
    elif operation == perform[5]:
        if b != 0:
            return a % b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(calculator(a, b, input("Enter the operation (+, -, *, /, **, %): ")))
