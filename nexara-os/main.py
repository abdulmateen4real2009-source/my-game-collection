import random
import json
import os
import time

SAVE_FILE = "save.json"

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def load_player():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)

    return {
        "name": "Agent Nova",
        "credits": 100,
        "xp": 0,
        "inventory": []
    }

def save_player(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f, indent=4)

player = load_player()

print("""
███╗   ██╗███████╗██╗  ██╗ █████╗ ██████╗  █████╗
████╗  ██║██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ███████║██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██╔══██║██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗██║  ██║██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

CYBERPUNK TERMINAL OS
""")

slow_print("Connecting to underground network...")
time.sleep(1)
slow_print("Access granted.\n")

while True:

    cmd = input("NEXARA > ").strip().lower()

    if cmd == "help":
        print("""
help        - show commands
profile     - view profile
scan        - scan network
hack        - perform hack
market      - buy upgrades
inventory   - show inventory
save        - save progress
quit        - exit game
""")

    elif cmd == "profile":
        print("\n=== PROFILE ===")
        print("Name:", player["name"])
        print("Credits:", player["credits"])
        print("XP:", player["xp"])

    elif cmd == "scan":
        targets = [
            "Corporate Server",
            "Government Node",
            "Crypto Exchange",
            "Darknet Vault",
            "Research Database"
        ]

        print("\nTargets Found:")
        for t in random.sample(targets, 3):
            print("-", t)

    elif cmd == "hack":

        print("\nLaunching exploit...")

        for i in range(0, 101, 20):
            print(f"{i}%")
            time.sleep(0.4)

        if random.random() > 0.3:
            reward = random.randint(100, 500)

            print("\nACCESS GRANTED")
            print(f"Credits Earned: {reward}")

            player["credits"] += reward
            player["xp"] += 50

        else:
            print("\nFIREWALL DETECTED")
            print("Hack Failed")

    elif cmd == "market":

        print("""
1. Password Cracker (300)
2. Quantum Decryptor (600)
3. Zero-Day Exploit (1000)
""")

        choice = input("Buy item number or ENTER: ")

        items = {
            "1": ("Password Cracker", 300),
            "2": ("Quantum Decryptor", 600),
            "3": ("Zero-Day Exploit", 1000)
        }

        if choice in items:

            item, cost = items[choice]

            if player["credits"] >= cost:
                player["credits"] -= cost
                player["inventory"].append(item)

                print(f"Purchased: {item}")
            else:
                print("Not enough credits.")

    elif cmd == "inventory":
        print("\nInventory:")

        if player["inventory"]:
            for item in player["inventory"]:
                print("-", item)
        else:
            print("Empty")

    elif cmd == "save":
        save_player(player)
        print("Game saved.")

    elif cmd == "quit":
        save_player(player)
        print("Disconnecting...")
        break

    else:
        print("Unknown command. Type 'help'.")
