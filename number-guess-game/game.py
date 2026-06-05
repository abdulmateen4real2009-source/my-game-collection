import random
from utils import get_guess

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🎮 Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break