import random
import json
import time
import os

SAVE_FILE = "data/save.json"

def load_save():
    try:
        with open(SAVE_FILE,"r") as f:
            return json.load(f)
    except:
        return {"highscore":1}

def save_game(highscore):
    with open(SAVE_FILE,"w") as f:
        json.dump({"highscore":highscore},f,indent=4)

def clear():
    os.system("clear")

save = load_save()
highscore = save["highscore"]

level = 1

print("=================================")
print("      MEMORY MATRIX")
print("=================================")
print("Remember the highlighted cells.")
print("Grid positions:")
print()
print("1 2 3")
print("4 5 6")
print("7 8 9")
input("\nPress ENTER to start...")

while True:

    clear()

    pattern_size = min(level + 2, 9)

    pattern = random.sample(range(1,10), pattern_size)

    print(f"\nLEVEL {level}")
    print()

    for i in range(1,10):

        if i in pattern:
            print("■", end=" ")
        else:
            print("□", end=" ")

        if i % 3 == 0:
            print()

    time.sleep(3)

    clear()

    print(f"\nLEVEL {level}")
    print()
    print("□ □ □")
    print("□ □ □")
    print("□ □ □")

    answer = input(
        "\nEnter remembered positions separated by spaces:\n> "
    )

    try:
        guess = list(
            map(int, answer.strip().split())
        )
    except:
        break

    if set(guess) == set(pattern):

        print("\nCORRECT!")
        level += 1

        if level > highscore:
            highscore = level
            save_game(highscore)

        time.sleep(1.5)

    else:

        print("\nWRONG!")
        print("Pattern was:", sorted(pattern))
        print("You reached Level", level)
        print("High Score:", highscore)

        break

print("\nThanks for playing!")
