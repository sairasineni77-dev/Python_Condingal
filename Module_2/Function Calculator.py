# Part 1: Four functions that each return an answer (def and return)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Part 4: Handles letters and dividing by zero (try / except / finally)
try:
    # Part 2: Asks for two numbers and an operation (input and float)
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    # Part 3: Calls the right function for the operation (if / elif / else)
    if operation == "+":
        print("Answer:", add(num1, num2))
    elif operation == "-":
        print("Answer:", subtract(num1, num2))
    elif operation == "*":
        print("Answer:", multiply(num1, num2))
    elif operation == "/":
        print("Answer:", divide(num1, num2))
    else:
        print("Invalid operation! Please enter +, -, *, or /.")

except ValueError:
    print("Oops! That was not a number. Please enter valid numbers next time.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
finally:
    print("Thank you for using the homework calculator!")
