import random
import json

SAVE_FILE = "data/save.json"

try:
    with open(SAVE_FILE) as f:
        highscore = json.load(f)["highscore"]
except:
    highscore = 0

player = {
    "health": 100,
    "gold": 0,
    "inventory": []
}

rooms_cleared = 0

monsters = [
    ("Goblin",20),
    ("Skeleton",30),
    ("Orc",40),
    ("Shadow Beast",50)
]

loot = [
    "Potion",
    "Sword",
    "Shield",
    "Gem",
    "Magic Scroll"
]

print("===================================")
print("         AI DUNGEON")
print("===================================")

while player["health"] > 0:

    rooms_cleared += 1

    print(f"\nRoom {rooms_cleared}")

    event = random.choice([
        "monster",
        "loot",
        "treasure"
    ])

    if event == "monster":

        monster,hp = random.choice(monsters)

        print(f"\nA {monster} appears!")

        while hp > 0 and player["health"] > 0:

            action = input(
                "Fight or Run? (f/r): "
            ).lower()

            if action == "f":

                damage = random.randint(10,25)
                hp -= damage

                print(
                    f"You hit for {damage}"
                )

                if hp > 0:

                    enemy_damage = random.randint(5,15)

                    player["health"] -= enemy_damage

                    print(
                        f"{monster} hits for {enemy_damage}"
                    )

            else:
                print("You escaped.")
                break

        if hp <= 0:
            reward = random.randint(20,60)

            player["gold"] += reward

            print(
                f"{monster} defeated!"
            )

            print(
                f"+{reward} gold"
            )

    elif event == "loot":

        item = random.choice(loot)

        player["inventory"].append(item)

        print(
            f"\nFound loot: {item}"
        )

    else:

        gold = random.randint(10,100)

        player["gold"] += gold

        print(
            f"\nFound treasure chest!"
        )

        print(
            f"+{gold} gold"
        )

    print("\n================")
    print("Health:", player["health"])
    print("Gold:", player["gold"])
    print("Inventory:", player["inventory"])
    print("================")

    choice = input(
        "\nContinue? (y/n): "
    ).lower()

    if choice != "y":
        break

if rooms_cleared > highscore:

    with open(SAVE_FILE,"w") as f:
        json.dump(
            {"highscore":rooms_cleared},
            f,
            indent=4
        )

print("\nGAME OVER")
print("Rooms Cleared:", rooms_cleared)
print("High Score:", max(highscore, rooms_cleared))
