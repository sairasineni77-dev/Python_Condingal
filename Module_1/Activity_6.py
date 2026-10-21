a = 10
b = 12
c = 15
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")



a = 0
b = -10
c = 0

if a > 0 or b > 0:
    print(" Either of one True")
else:
    print("Both are False")



a = 10
b = 12
c = 12

print(not (a == b))

a = "python"
b = "coding"

if not (a == b):
    print(a, "and", b, "are different.")

    a = 4
    b = 5

    if not ((a == 1) == (b == 5)):
        print("Hello")

a = int(input("Enter a number: "))

if not (a % 2 == 0):
    print(a, "is an odd number.")


height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("ou are severly over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")