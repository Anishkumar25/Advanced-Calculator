import math

def save_history(expression, result):
    with open("history.txt", "a") as file:
        file.write(f"{expression} = {result}\n")

def show_history():
    try:
        with open("history.txt", "r") as file:
            history = file.readlines()
            if not history:
                print("History is empty.")
            else:
                print("History:")
                for line in history:
                    print(line, end="")
    except FileNotFoundError:
        print("History is empty.")

def add(x, y):
    result = x + y
    save_history(f"{x} + {y}", result)
    return result

def subtract(x, y):
    result = x - y
    save_history(f"{x} - {y}", result)
    return result

def multiply(x, y):
    result = x * y
    save_history(f"{x} * {y}", result)
    return result

def divide(x, y):
    if y == 0:
        return "Can't divide by zero!"
    result = x / y
    save_history(f"{x} / {y}", result)
    return result

def power(x, y):
    result = x ** y
    save_history(f"{x} ** {y}", result)
    return result

def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers."
    if x == 0 or x == 1:
        return 1
    fact = 1
    for i in range(2, x + 1):
        fact *= i
    result = fact
    save_history(f"{x}!", result)
    return result

def sqrt(x):
    if x < 0:
        return "Square root is not defined for negative numbers."
    result = math.sqrt(x)
    save_history(f"sqrt({x})", result)
    return result

def log(x):
    if x <= 0:
        return "Logarithm is not defined for non-positive numbers."
    result = math.log(x)
    save_history(f"log({x})", result)
    return result

def trigonometry(x, func):
    if func == 'sin':
        result = math.sin(x)
        save_history(f"{func}({x})", result)
        return result
    elif func == 'cos':
        result = math.cos(x)
        save_history(f"{func}({x})", result)
        return result
    elif func == 'tan':
        result = math.tan(x)
        save_history(f"{func}({x})", result)
        return result
    elif func == 'csc':
        result = 1 / math.sin(x)
        save_history(f"{func}({x})", result)
        return result
    elif func == 'sec':
        result = 1 / math.cos(x)
        save_history(f"{func}({x})", result)
        return result
    elif func == 'cot':
        result = 1 / math.tan(x)
        save_history(f"{func}({x})", result)
        return result
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
        print("10. Show history")
        print("11. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): ")

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
        elif choice == '10':
            show_history()
        elif choice == '11':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

calculator()