#Take input of a word
string = input("Please enter your own word : ")
#take input of a character
char = input("Please enter your own Character : ")
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(string)): #string operation
    print("The value of i before execution", i)
    if(string[i] == char): #condition 1
        print("The value of count before changing", count)
        count = count + 1
        print("The value of count after changing", count)
    
    print("The value of the character", string[i])
    i = i + 1
    print("The value of i after increment", i)

#Display the result
print("The total Number of Times ", char, " has Occurred = " , count)

lower = int(input("enter a lower range: "))
upper = int(input("enter a upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range (lower, upper, + 1):
    if num > 1:
        for i in range(2, num):
            if (num % 1) == 0:
                break
        else:
            print(num)
            
