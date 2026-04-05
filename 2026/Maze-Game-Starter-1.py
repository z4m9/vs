# 🧩 MAZE GAME STARTER
# Year 11SE AT1 Programming Fundamentals

# You will build and improve this program across the unit.
# By the end, your game should include:
# ✔ at least 8 rooms
# ✔ items you can collect 🎒
# ✔ scoring ⭐
# ✔ save/load 💾
# ✔ clear instructions for the user

# 💡 You CAN use emojis in descriptions and messages!


# ----------------------------------
# 🗺️ ROOMS (ADD MORE APPROPRIATE TO YOUR THEME)
# ----------------------------------
rooms = {
    "Room1": {
        "desc": "Description appropriate to theme.",
        "up": "Room2"
    },

    "Room2": {
        "desc": "A long hallway stretches ahead.",
        "down": "Room1"
    }

    # 👉 ADD MORE ROOMS
    # You need at least 8 rooms for the task
}

# 🎒 Items you collect will go here
inventory = []

# ⭐ You will create a scoring system later
score = 0


# ----------------------------------
# 🎮 INTRO + HELP
# ----------------------------------
def show_intro():
    print("\n🏁 Welcome to the Maze Game!")
    print("Explore the maze, collect items and earn points.")
    print("Type 'help' to see commands.\n")


def show_help():
    print("\n📜 Commands you can use:")
    print("  up / down / left / right  ➡️  move between rooms")
    print("  help                      ❓ show commands")
    print("  quit                      🚪 exit the game")

    # 👉 Add more commands such as:
    # inventory
    # pick up item
    # save
    # load
    # score
    # map


# ----------------------------------
# 📍 SHOW CURRENT ROOM
# ----------------------------------
def show_room(current_room):
    print(f"\n📍 You are in {current_room}.")
    print(rooms[current_room]["desc"])

    # 👉 When you add items to rooms,
    # you can show them here like this:
    #
    # if "items" in rooms[current_room]:
    #     print("You see:", ", ".join(rooms[current_room]["items"]), "👀")


# ----------------------------------
# 🚶 MOVE BETWEEN ROOMS
# ----------------------------------
def move(direction, current_room):

    # Check if the direction exists in this room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        print(f"\n🚶 You move {direction} to {new_room}.")
        return new_room

    # If the direction is not valid
    print("\n⛔ You can't go that way!")
    return current_room


# ----------------------------------
# 🔁 MAIN GAME LOOP
# ----------------------------------
def game_loop():

    # Starting room
    current_room = "Room1"

    show_intro()

    while True:

        show_room(current_room)

        # Ask the player for a command
        command = input("\n> ").strip().lower()

        # Movement commands
        if command in ("up", "down", "left", "right"):
            current_room = move(command, current_room)

        # Show help
        elif command == "help":
            show_help()

        # Quit game
        elif command == "quit":
            print("\n👋 Thanks for playing!")
            break

        # Anything else = invalid
        else:
            print("\n❌ Invalid command.")
            show_help()


# ----------------------------------
# ▶️ START GAME
# ----------------------------------
if __name__ == "__main__":
    game_loop()
