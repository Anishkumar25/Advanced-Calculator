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

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")    
        print("4. Divide")
        print("5. Power")
        print("6. Factorial")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

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
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

calculator()
