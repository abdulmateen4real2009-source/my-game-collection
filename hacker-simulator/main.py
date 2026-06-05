import json
import random
import os

SAVE_FILE = "saves/player.json"

MISSIONS = [
    {
        "id": 1,
        "name": "Network Scan",
        "description": "Scan a target network.",
        "xp": 50,
        "credits": 100
    },
    {
        "id": 2,
        "name": "Password Audit",
        "description": "Audit weak passwords.",
        "xp": 100,
        "credits": 200
    },
    {
        "id": 3,
        "name": "Server Investigation",
        "description": "Investigate a suspicious server.",
        "xp": 150,
        "credits": 300
    }
]

RANKS = [
    (0, "Script Kiddie"),
    (100, "Junior Operator"),
    (300, "Network Analyst"),
    (600, "Cyber Specialist"),
    (1000, "Elite Hacker")
]

def load_player():
    with open(SAVE_FILE) as f:
        return json.load(f)

def save_player(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f, indent=4)

def update_rank(player):
    for xp_needed, rank in reversed(RANKS):
        if player["xp"] >= xp_needed:
            player["rank"] = rank
            return

def show_profile(player):
    print("\n==============================")
    print(" NEXARA HACKER PROFILE ")
    print("==============================")
    print("Rank:", player["rank"])
    print("XP:", player["xp"])
    print("Credits:", player["credits"])
    print("Completed Missions:", len(player["missions_completed"]))
    print("==============================\n")

def perform_scan():
    print("\nScanning network...")
    for i in range(5):
        ip = f"192.168.1.{random.randint(1,254)}"
        print("Found Host:", ip)

def run_mission(player):
    print("\nAvailable Missions:\n")

    for mission in MISSIONS:
        if mission["id"] not in player["missions_completed"]:
            print(
                f"{mission['id']}. {mission['name']} "
                f"(XP {mission['xp']} | Credits {mission['credits']})"
            )

    choice = input("\nMission ID: ")

    try:
        mission_id = int(choice)
    except:
        return

    mission = next(
        (m for m in MISSIONS if m["id"] == mission_id),
        None
    )

    if not mission:
        print("Mission not found.")
        return

    if mission["id"] in player["missions_completed"]:
        print("Mission already completed.")
        return

    print("\nMission:", mission["name"])
    print(mission["description"])

    if mission["id"] == 1:
        perform_scan()

    elif mission["id"] == 2:
        print("\nChecking password database...")
        print("Weak passwords detected!")

    elif mission["id"] == 3:
        print("\nInvestigating server logs...")
        print("Suspicious activity found!")

    print("\nMISSION SUCCESSFUL")

    player["xp"] += mission["xp"]
    player["credits"] += mission["credits"]

    player["missions_completed"].append(mission["id"])

    update_rank(player)
    save_player(player)

def main():

    player = load_player()

    while True:

        print("\n========== NEXARA ==========")
        print("1. Profile")
        print("2. Missions")
        print("3. Network Scan")
        print("4. Exit")
        print("============================")

        choice = input("> ")

        if choice == "1":
            show_profile(player)

        elif choice == "2":
            run_mission(player)

        elif choice == "3":
            perform_scan()

        elif choice == "4":
            save_player(player)
            print("\nSession Saved.")
            break

if __name__ == "__main__":
    main()
