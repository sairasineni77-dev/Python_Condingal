a = input ("Enter a word: ")

for i in a:
    if (i == "A"):
        print ("A is found")
        break
    else:
        print ("A is not found")

for x in range(10):
    if x % 20 == 0:
        print("twist")

    elif x % 15 == 0:
        pass

    elif x % 5 == 0:
        print("buzz")

    else:
        print(x)