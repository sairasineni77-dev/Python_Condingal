def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1,2,3,4 or +, -, *, /): ")
if choice in ("1", "2", "3", "4", "+", "-", "*", "/"):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter a second number: "))

        if choice in ("1", "+"):
            print("Result:", add(num1, num2))
        
        elif choice in ("2", "-"):
            print("Result:", subtract(num1, num2))

        elif choice in ("3", "*"):
            print("Result:", multiply(num1, num2))

        elif choice in ("4", "/"):
            print("Result:", divide(num1, num2))

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid operation selected.")