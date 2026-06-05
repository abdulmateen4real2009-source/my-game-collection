def get_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()

        if choice in ["rock", "paper", "scissors"]:
            return choice

        print("Invalid choice. Try again.")
