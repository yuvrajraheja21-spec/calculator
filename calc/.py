# calculator
this is my second project where i had made calculator 
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
text= int(input("Enter a number for the loop: "))
perform= input("Enter the operation (+, -, *, /): ")
if perform == '+':
    result = a + b
    print("The result is:", result)
elif perform == '-':
    result = a - b
    print("The result is:", result)
elif perform == '*':
    result = a * b
    print("The result is:", result)
elif perform == '/':
    if b != 0:
        result = a / b
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else: 
    print("Invalid operation. Please enter one of the following: +, -, *, /.")
print("Thank you for using the calculator!")
for i in range(text):
    print("This is number:", i + 1)
