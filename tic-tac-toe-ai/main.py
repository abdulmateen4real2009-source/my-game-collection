import json
import random

SCORES_FILE = "data/scores.json"

def load_scores():
    try:
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    except:
        return {"wins":0,"losses":0,"draws":0}

def save_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def print_board(board):
    print()
    for i in range(0,9,3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print()

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def board_full(board):
    return " " not in board

def ai_move(board):
    available = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available)

scores = load_scores()

while True:

    board = [" "] * 9

    print("\n=== TIC TAC TOE AI ===")
    print("You = X")
    print("AI  = O")

    while True:

        print_board(board)

        try:
            move = int(input("Choose position (1-9): ")) - 1
        except:
            continue

        if move < 0 or move > 8 or board[move] != " ":
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            scores["wins"] += 1
            break

        if board_full(board):
            print_board(board)
            print("Draw!")
            scores["draws"] += 1
            break

        ai = ai_move(board)
        board[ai] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            scores["losses"] += 1
            break

        if board_full(board):
            print_board(board)
            print("Draw!")
            scores["draws"] += 1
            break

    save_scores(scores)

    print("\nStatistics")
    print("Wins :", scores["wins"])
    print("Losses :", scores["losses"])
    print("Draws :", scores["draws"])

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        break
