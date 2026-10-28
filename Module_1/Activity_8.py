n = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i
    print("\nsum =", sum)


string = input("Please enter your own string")
string2 = (" ")
for i in string:
    print(i)
    string2 = i + string2

print("\nThe Original String = ", string)
print("The Reversed String = ", string2)
