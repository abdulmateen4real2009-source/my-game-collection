import random

locations = {
    "forest": "You are in a dark forest. Trees surround you.",
    "cave": "You enter a mysterious cave. It's cold and damp.",
    "village": "You arrive at a small village. People seem nervous."
}

current_location = "forest"
health = 100
inventory = []

print("=" * 50)
print("🤖 AI ADVENTURE")
print("=" * 50)
print("Type actions like:")
print("- explore")
print("- search")
print("- attack")
print("- run")
print("- inventory")
print("- quit")
print()

while True:
    print(f"\n📍 {current_location.upper()}")
    print(locations[current_location])

    action = input("\nWhat do you do? > ").lower().strip()

    if action == "quit":
        print("👋 Thanks for playing!")
        break

    elif action == "inventory":
        print(f"🎒 Inventory: {inventory if inventory else 'Empty'}")

    elif "explore" in action:
        current_location = random.choice(list(locations.keys()))
        print("🚶 You travel to a new location.")

    elif "search" in action:
        loot = random.choice([
            "Gold Coin",
            "Magic Ring",
            "Sword",
            "Potion",
            None
        ])

        if loot:
            inventory.append(loot)
            print(f"✨ You found: {loot}")
        else:
            print("🔍 You found nothing.")

    elif "attack" in action:
        enemy = random.choice(["Goblin", "Wolf", "Bandit"])

        if random.random() > 0.4:
            print(f"⚔️ You defeated the {enemy}!")
            reward = random.randint(5, 20)
            print(f"🏆 Gained {reward} XP")
        else:
            damage = random.randint(5, 15)
            health -= damage
            print(f"💥 The {enemy} hit you for {damage} damage.")
            print(f"❤️ Health: {health}")

            if health <= 0:
                print("☠️ Game Over")
                break

    elif "run" in action:
        print("🏃 You escaped safely.")

    else:
        responses = [
            "🤖 I don't understand that action.",
            "🤖 Try exploring or searching.",
            "🤖 Nothing happens."
        ]
        print(random.choice(responses))
