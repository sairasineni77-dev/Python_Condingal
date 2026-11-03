print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))

for i in range(n):
    for j in range (i+1):
        print("* ", end="")
    print()



rows = int(input("Please Enter the total Number of Rows :"))
number = 1

print("Floyd's Triangle")
for i in range(1, rows + 1):
    for j in range (1, i + 1):
        print(number, end = " ")
        number = number + 1
    print()
    