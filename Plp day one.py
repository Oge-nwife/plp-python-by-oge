print ["hello,what's your name"]
name =input()
print ["welcome, name:"]
num1 =float(input("enter the first number:"))
num2 =float(input("enter second number:"))
operation = input("enter an operation(+,-,*,/):")

if operation == "+":
    result = num1 + num2
elif operation == "-":
        result =num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print("result: {num1} {operation}{num2} = {result}") 
ValueError: any

print("Error:please enter valid numbers.")






