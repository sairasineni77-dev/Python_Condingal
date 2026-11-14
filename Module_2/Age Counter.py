try:
    age = int(input("Enter your age: "))
    
    if age % 2 == 0:
        print("The age entered is even.")
    else:
        print("The age entered is odd.")

except ValueError:
    print("Value Error: Please enter a valid whole number for your age.")
