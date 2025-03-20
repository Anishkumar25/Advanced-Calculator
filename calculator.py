def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Can't divide by zero!"
    return x / y
def power(x, y):
    return x ** y
def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers."
    if x == 0 or x == 1:
        return 1
    fact = 1
    for i in range(2, x + 1):
        fact *= i
    return fact
import math

def sqrt(x):
    if x < 0:
        return "Square root is not defined for negative numbers."
    return math.sqrt(x)
def log(x):
    if x <= 0:
        return "Logarithm is not defined for non-positive numbers."
    return math.log(x)
def trigonometry(x, func):
    if func == 'sin':
        return math.sin(x)
    elif func == 'cos':
        return math.cos(x)
    elif func == 'tan':
        return math.tan(x)
    elif func == 'csc':
        return 1 / math.sin(x)
    elif func == 'sec':
        return 1 / math.cos(x)
    elif func == 'cot':
        return 1 / math.tan(x)
    else:
        return "Invalid trigonometric function!"

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")    
        print("4. Divide")
        print("5. Power")
        print("6. Factorial")
        print("7. Square root")
        print("8. Logarithm")
        print("9. Trigonometry")
        print("10. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))    
            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
            elif choice == '5':
                print("Result: ", power(num1, num2))

        elif choice == '6':
            num = input("Enter a non-negative integer: ")
            if num.isdigit():  # Ensures only positive integers
                print("Result: ", factorial(int(num)))
            else:
                print("Invalid input! Please enter a non-negative integer.")
        elif choice == '7':
            num = float(input("Enter a non-negative number: "))
            print("Result: ", sqrt(num))
        elif choice == '8': 
            num = float(input("Enter a positive number: "))
            print("Result: ", log(num))
        elif choice == '9':
            num = float(input("Enter an angle in radians: "))
            func = input("Enter trigonometric function (sin/cos/tan/csc/sec/cot): ")
            print("Result: ", trigonometry(num, func))

        elif choice == "10":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

calculator()
