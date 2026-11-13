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

import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock, paper, scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    break

import math #importing math module
#using ceil and floor functiom of math module
print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))
print("===")
print(math.ceil(23.56))
print(math.floor(23.56))
x = 10
y = -15
#using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

#using fabs and gcd function
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))  