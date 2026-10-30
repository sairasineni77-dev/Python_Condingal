n = int(input("Enter the value of terms: "))

sum = 0
i = 1
while i<=n: 
    sum = sum+i
    i = i+1
    print(sum)
    print(i)

print("\nsum =", sum)


i = 0
while i<=0:
    print("I WILL RUN FOREVER")
    print("The value of i", i)
    i = i+1



num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    print("The value of digit", digit)
    sum += digit ** 3
    print("The value of sum", sum)
    temp //= 10
    print("The value of temp", temp)

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not a Armstrong number")
    
