import random
print(random.choice('computer'))

import random
# using random() to generate a random number
# between 0 and 1
print("The random number between 0 and 1 is : ", end="")

print(random.random())

# using seed() to seed a random number
print(random.seed(4))
print(random.random())

# Number Game
playing = True
number = str(random.randint(0,9))
print(number)
print("I will generate a number from 0 to 9")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break

    else:
        print("Your guess isn't quite right, try again. \n")