#1.Prime Number
num = int(input("Enter a number: "))

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
    
    

#2.Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci(100)


#3.Factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  
print(factorial(0))  




#4. Calculator
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operator. Use +, -, *, or /"

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        
        result = calculator(num1, num2, operator)
        print(f"Result: {result}")
    
        again = input("Do another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
    except ValueError:
        print("Error: Please enter valid numbers.")