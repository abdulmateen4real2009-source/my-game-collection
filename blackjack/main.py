import random
import json

SAVE_FILE = "data/player.json"

def load_player():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "credits":1000,
            "wins":0,
            "losses":0,
            "draws":0
        }

def save_player(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f, indent=4)

def create_deck():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    deck = cards * 4
    random.shuffle(deck)
    return deck

def hand_value(hand):
    value = sum(hand)

    aces = hand.count(11)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

player = load_player()

while True:

    print("\n===================")
    print(" BLACKJACK ")
    print("===================")
    print("Credits:", player["credits"])
    print("Wins:", player["wins"])
    print("Losses:", player["losses"])
    print("Draws:", player["draws"])

    try:
        bet = int(input("\nBet Amount: "))
    except:
        continue

    if bet <= 0 or bet > player["credits"]:
        continue

    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:

        print("\nYour Hand:", player_hand)
        print("Value:", hand_value(player_hand))

        print("Dealer Shows:", dealer_hand[0])

        if hand_value(player_hand) > 21:
            print("BUST!")
            player["credits"] -= bet
            player["losses"] += 1
            break

        action = input("\nHit or Stand? (h/s): ").lower()

        if action == "h":
            player_hand.append(deck.pop())
        else:
            break

    if hand_value(player_hand) <= 21:

        while hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())

        print("\nDealer Hand:", dealer_hand)
        print("Dealer Value:", hand_value(dealer_hand))

        p = hand_value(player_hand)
        d = hand_value(dealer_hand)

        if d > 21 or p > d:
            print("YOU WIN!")
            player["credits"] += bet
            player["wins"] += 1

        elif p < d:
            print("YOU LOSE!")
            player["credits"] -= bet
            player["losses"] += 1

        else:
            print("DRAW!")
            player["draws"] += 1

    save_player(player)

    if player["credits"] <= 0:
        print("\nGAME OVER - OUT OF CREDITS")
        break

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        break

save_player(player)
