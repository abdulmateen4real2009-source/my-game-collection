import random
from utils import get_choice

choices = ["rock", "paper", "scissors"]

def play_game():
    print("🎮 Rock Paper Scissors")
    print("Type rock, paper, or scissors")
    print()

    while True:
        player = get_choice()
        computer = random.choice(choices)

        print(f"\nYou: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("🤝 Draw!")

        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("🎉 You Win!")
        else:
            print("💀 You Lose!")

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break
