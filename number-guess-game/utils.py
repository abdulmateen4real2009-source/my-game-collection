def get_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")