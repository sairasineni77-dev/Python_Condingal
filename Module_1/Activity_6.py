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