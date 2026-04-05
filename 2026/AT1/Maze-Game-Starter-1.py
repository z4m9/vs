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
    "Room 1": {
        "desc": "A hint of light is visible ahead.",
        "forward": "Room 2"
    },
    "Room 2": {
        "desc": "A long wooden bridge stretches ahead, but there is a pile of rocks in the way.",
        "backward": "Room 1",
        "left": "Room 3",
        "right": "Room 4",
        "forward": "Room 5"
    },
    "Room 3": {
        "desc": "An item lies in front of you.",
        "right": "Room 2",
        "up": "Room 6"
    },
    "Room 4":{
        "desc": "An item lies in front of you.",
        "left": "Room 2",
        "forward": "Room 7"
    },
    "Room 5": {
        "desc": "A massive cave surrounds."
        "Decide where to go carefully, as one of the bridges will collapse beneath you.",
        "left": "Room 6",
        "right": "Room 7",
        "forward": "Room 10",
        "backward": "Room 2"
    },
    "Room 6": {
        "desc": "An item lies and a locked door is in front. You must find the key that opens it.",
        "forward": "Room 9",
        "backward": "Room 3",
        "right": "Room 5"
    },
    "Room 7": {
        "desc": "There is a wave of mobs preventing you from getting further. You must defeat the mobs.",
        "forward": "Room 8",
        "backward": "Room 4",
        "left": "Room 5"
    },
    "Room 8":{
        "desc": "There is a locked door to the right. You must find the key that opens it."
        "There is another key just beneath you, this is for the door in Room 6. ",
        "backward": "Room 7",
        "left": "Room 10"
    },
    "Room 9": {
        "desc": "A set of something and a bottle lies beneath you.",
        "right": "Room 10",
        "backward": "Room 6"
    },
    "Room 10": {
        "desc": "There is a monster preventing you from getting the key for the Room 8 door."
        "You must defeat the monster.",
        "left": "Room 9",
        "right": "Room 8",
        "backward": "Room 5"
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
    print("- forward / backward / left / right \n ➡️ move between rooms")
    print("- help                   \n ❓ show commands")
    print("- quit                   \n 🚪 exit the game")
    print("- inventory              \n 🎒 check your inventory")
    print("- pick up item           \n 🧹 collect item")
    print("- save                   \n 🛟 save your progress")
    print("- load                   \n 💾 load your saved progress")
    print("- score                  \n ⭐  check how many points you have")
    print("- map                    \n 🗺️  show map of your current location")

    # 👉 Add more commands such as:
    # inventory
    # pick up item
    # save
    # load
    # score
    # map

# ----------------------------------
# 💾 LOAD/SAVE GAME & SCORE
# ----------------------------------
def save_game(current_room, inventory, score):
    inventory = []
    with open("save_file.txt", "w") as game_file:
        game_file.write(current_room + "\n") # Save the current room on the first line
        game_file.write(",".join(inventory)) # Save inventory items as a comma_separated list
    with open("score.txt", "w") as score_file:
        score_file.write(str(score))

    print("\n 💾 Game saved successfully!")

def load_game():
    global inventory
    try:
        with open("save_file.txt", "r") as file:
            lines = file.readlines()
            room = lines[0].strip() # Read the first line for the current room
            if len(lines) > 1: # Read inventory
                inventory = lines[1].strip().split(",")
            else:
                inventory = []

        
        with open("score.txt", "r") as score_file:
            score = int(score_file.read().strip())

        print("\n 💾 Game loaded successfully!")
        return room, score
    except FileNotFoundError:
        print("\n ⚠️ No saved file found. Starting new game...")
        return "Room 1", 0 # Default starting room and score

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
        
        # Load saved progress
        elif command == "load":
            load_game()
        
        # Save game
        elif command == "save":
            save_game(current_room, inventory, score)

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
