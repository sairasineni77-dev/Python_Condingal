import random

secret = random.randint(1, 20)
lives = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")

# Part 1: Ask for a guess, up to 5 times (while loop, int(input()))
while lives > 0:
    # Part 4: Show hearts for lives left (for loop)
    hearts = ""
    for i in range(lives):
        hearts = hearts + "❤️ "
    print("\nLives left:", hearts)

    guess = int(input("Enter your guess: "))
    diff = abs(secret - guess)

    # Part 2: Say if the guess is right (if / else)
    if guess == secret:
        print("Congratulations! You guessed the right number!")
        break
    else:
        lives = lives - 1
        
        # Part 3: Give a hint: Ice cold, Cold, Warm or Hot (if / elif / else)
        if lives > 0:
            if diff <= 2:
                print("Hint: Hot!")
            elif diff <= 5:
                print("Hint: Warm")
            elif diff <= 10:
                print("Hint: Cold")
            else:
                print("Hint: Ice cold")

# Part 4: Game over message when all 5 lives run out
if lives == 0:
    print("\nGame over! The secret number was", secret)


