import random

print("Welcome to the Number Guessing Game...")
print("I am thinking of a Number between 1 and 100.")

number = random.randint(1, 100)

level = input("Choose a difficulty Type 'easy' or 'hard': ").lower()

if level == 'easy':
    attempt = 10
elif level == 'hard':
    attempt = 5

while attempt > 0:
    print(f"You have {attempt} attempts remaining to guess the Number.")
    user_guess = int(input("Make a Guess: "))

    if user_guess < number:
        print("Too low.")
        print("Guess Again.")
    elif user_guess > number:
        print("Too high.")
        print("Guess Again.")
    else:
        print(f"You guessed it right!! The answer was {number}")
        break
    
    attempt -= 1

if attempt == 0:
    print("You've run out of guesses, You lose!!")