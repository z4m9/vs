# 🧩 MAZE GAME
# Year 11SE AT1 Programming Fundamentals

# You will build and improve this program across the unit.
# By the end, your game should include:
# ✔ at least 8 rooms
# ✔ items you can collect 🎒
# ✔ scoring ⭐
# ✔ save/load 💾
# ✔ clear instructions for the user

# 💡 You CAN use emojis in descriptions and messages!

# Samuel Marriott
# Started: 5/04/2026
# Due finish: 24/04/2026
# Finished: Date/Month/2026

# Bibliography/references:
# https://www.w3schools.com/python/ref_func_print.asp

# ----------------------------------
# 🗺️ ROOMS (ADD MORE APPROPRIATE TO YOUR THEME)
# ----------------------------------
rooms = {}
def init_rooms():
    global rooms
rooms = {
    "Room 1 - Start": {
        "desc": "A hint of light is visible ahead.",
        "forward": "Room 2",
        "pos": {"r": 21, "c": 24}
    },
    "Room 2": {
        "desc": "A long wooden bridge stretches ahead, but there is a pile of rocks in the way.",
        "backward": "Room 1",
        "left": "Room 3",
        "right": "Room 4",
        "forward": "Room 5",
        "pos": {"r": 14, "c": 24},
        "rocksfall": True,
        "rocksfall_pos": {"r": 11, "c": 24}
    },
    "Room 3": {
        "desc": "An item lies on your left.",
        "item": "🔑 key",
        "right": "Room 2",
        "forward": "Room 6",
        "pos": {"r": 14, "c": 6}
    },
    "Room 4":{
        "desc": "An item lies in front of you, and there is a locked door behind. "
        "\nYou must find the ancient key that opens it.",
        "requires": "🔑 key",
        "item": "⛏️ pickaxe",
        "left": "Room 2",
        "forward": "Room 7",
        "backward": "Room 11 - Finish",
        "pos": {"r": 14, "c": 46},
        "archr_monster": True,
        "archr_mon_pos": {"r": 12, "c": 40}
    },
    "Room 5": {
        "desc": "A massive cave surrounds. "
        "Decide where to go carefully, as one of the bridges will collapse beneath you.",
        "item": "🛡️ shield",
        "requires": "⛏️ pickaxe",
        "left": "Room 6",
        "right": "Room 7",
        "forward": "Room 10",
        "backward": "Room 2",
        "pos": {"r": 8, "c": 25}
    },
    "Room 6": {
        "desc": "An item lies and a monster is in front. You must find the weapon that defeats it. "
        "Note: The key is not the item that lies in front.",
        "item": "🗡️ sword",
        "forward": "Room 9",
        "backward": "Room 3",
        "right": "Room 5",
        "pos": {"r": 8, "c": 5},
        "archr_monster": True,
        "archr_mon_pos": {"r": 5, "c": 4}
    },
    "Room 7": {
        "desc": "There is a wave of mobs preventing you from getting further."
        "Use your sword to defeat the mobs. Use your shield to deflect their attacks.",
        "item": "🧪 regeneration potion",
        "requires": "🗡️ sword",
        "forward": "Room 8",
        "backward": "Room 4",
        "left": "Room 5",
        "pos": {"r": 8, "c": 48},
        "sword_monster": True,
        "sword_mon_pos": {"r": 2, "c": 31}
    },
    "Room 8":{
        "desc": "",
        "requires": "🧪 regeneration potion",
        "item": "🏹 bow & arrows",
        "backward": "Room 7",
        "left": "Room 10",
        "pos": {"r": 2, "c": 44}
    },
    "Room 9": {
        "desc": "The apex predator is in the room to your right.",
        "item": "💎 gemstone",
        "requires": "🏹 bow & arrows",
        "right": "Room 10",
        "backward": "Room 6",
        "pos": {"r": 2, "c": 4}
    },
    "Room 10": {
        "desc": "Well done! You have successfully defeated the apex predator."
        "Go back to Room 4 and unlock the door to finish the game."
        "You must defeat the monster.",
        "requires": "🛡️ shield",
        "item": "🗝️ ancient key",
        "left": "Room 9",
        "right": "Room 8",
        "backward": "Room 5",
        "pos": {"r": 2, "c": 21},
        "apex_predator": True,
        "apex_pred_pos": {"r": 2, "c": 14},
        "sword_monster": True,
        "sword_mon_pos": {"r": 3, "c": 16}
    },
    "Room 11 - Finish": {
        "desc": "Well done! You have successfully made it out of the mineshaft.",
        "requires": "🗝️ ancient key",
        "pos": {"r": 20, "c": 46}
    }
}

# Items collected will go here
inventory = []

# ⭐  scoring system 
score = 0

# ----------------------------------
# 🎮 INTRO + HELP
# ----------------------------------
def show_intro():
    print("\n🏁 Welcome to the Maze Game!")
    print("Explore the maze, collect items and earn points.")
    print("You must go to each room in numerical order.")
    print("There will be entities preventing you from skipping numbers.")
    print("Type 'help' to see commands.\n")


def show_help():
    print("\n📜 Commands you can use:")
    print(" forward / backward / left / right \n\t➡️ move between rooms")
    print(" help                   \n\t❓ show commands")
    print(" quit                   \n\t🚪 exit the game")
    print(" inventory              \n\t🎒 check your bag")
    print(" pick up                \n\t🧹 collect item")
    print(" save                   \n\t🛟 save your progress")
    print(" load                   \n\t💾 load your saved progress")
    print(" score                  \n\t⭐  check how many points you have")
    print(" map                    \n\t🗺️  show map of your current location")
    print(" use                    \n\tuse the desired item")
    print("You may wonder, 'How do I use the items I collected? '" \
    "\nThe answer is, use, or sometimes your character will \nautomatically use the item based on the circumstance. " \
    "\ne.g: If there is a locked door and the player has a key in their \ninventory," \
    " then the key will be used automatically to open that door.")

# ----------------------------------
# 💾 LOAD/SAVE GAME & SCORE
# ----------------------------------
def save_game(current_room, inventory):
    with open("maze_game.txt", "w") as game_file:
        game_file.write(current_room + "\n") # Save the current room on the first line
        game_file.write(",".join(inventory)) # Save inventory items as a comma_separated list
    with open("maze_game_score.txt", "w") as score_file:
        score_file.write(str(score))

    print("\n\t💾 Game saved successfully!")

def load_game():
    global inventory
    global score
    try:
        with open("maze_game.txt", "r") as game_file:
            lines = game_file.readlines()
            room = lines[0].strip() # Read the first line for the current room
            if len(lines) > 1: # Read inventory
                inventory = lines[1].strip().split(",")
            else:
                inventory = []
        
        with open("maze_game_score.txt", "r") as score_file:
            score = int(score_file.read().strip())

        print("\n\t💾 Game loaded successfully!")
        return room
    except FileNotFoundError:
        print("\n\t⚠️ No saved file found. Starting new game...")
        return "Room 1 - Start", 0 # Default starting room and score

# ----------------------------------
# 🗺️ MAP
# ----------------------------------
# COLUMNS          10        20        30        40        50
        #01234567890123456789012345678901234567890123456789       
def map(current_room):
    map = [                                                     # ROWS
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n", # 0
        "▒💡       ▒                    ▒               💡▒\n", # 1
        "▒  💎               🗝️                     🏹   ▒\n", # 2
        "▒         ▒                    ▒                 ▒\n", # 3
        "▒         ▒                    ▒                 ▒\n", # 4
        "▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒🪤 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 5
        "▒        ▒💡                   ▒                 ▒\n", # 6 
        "▒        ▒                     ▒                 ▒\n", # 7
        "▒  🗡️                  🛡️                     🧪   ▒\n", # 8
        "▒        ▒                     ▒                 ▒\n", # 9
        "▒💡      ▒                     ▒                 ▒\n", # 10
        "▒▒▒▒🪤 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 11
        "▒             ▒💡                ▒💡             ▒\n", # 12
        "▒             ▒                  ▒               ▒\n", # 13
        "▒    🔑                          🚪           ⛏️  ▒\n", # 14
        "▒💡           ▒                  ▒               ▒\n", # 15
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒🚪▒\n", # 16
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 17
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 18
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 19
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 20
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n"  # 21
    ]
    # Legend
    print("\n\tLegend:" \
    "\n\t👿: Monster, defeat with a sword only. " \
    "\nWill throw you back into the current room if you fail to do so." \
    "\n\t웃: Your character, each time you want to see the map," \
    "\n\tyour character will be displayed in its current position." \
    "\n\t👾: Monster, defeat with a bow and arrows only. " \
    "\nWill throw you back into the current room if you fail to do so." \
    "\n\t👹: Apex predator, defeat with a bow and arrows and a sword." \
    "\n\t🚪: Locked door, use items collected to open these." \
    "\n\t💎: Gems, must be collected to repair weapons and armory." \
    "\n\t🪨 : Rocks, must be cleared to progress." \
    "\n\t🪤 : Traps, you will die if you walk into these." \
    "\n\t💡: Lights, will help you to navigate through the dark passages."
    "\n\tThe other symbols are items. \nYou need these to unlock doors or defeat monsters.")
    print("The numbers in each room are the room numbers. \n\tYou must visit each room in numerical order.\n")

    current_pos = {"r": rooms[current_room]["pos"]["r"], "c": rooms[current_room]["pos"]["c"]}
    show_map(map, current_pos)

def show_map(map, player_pos):
    r = 0  # row zero
    player_icon = "웃"
    rocksfall_icon = "🪨"
    sword_monster_icon = "👿"
    archr_monster_icon = "👾"
    apex_predator_icon = "👹"
    rows = len(map)
    while r < rows:         # iterate through each row
        c = 0
        rowString = map[r]
        rowlen = len(rowString)
        while c < rowlen:  # print each column in row
            if c == player_pos["c"] and r == player_pos["r"]:
                print(player_icon, end = "") 
                c += 1 # double wide character, so move to next column.
            elif c == rooms["Room 2"]["rocksfall_pos"]["c"] and r == rooms["Room 2"]["rocksfall_pos"]["r"] and rooms["Room 2"]["rocksfall"]:
                print(rocksfall_icon, end = "")
            elif c == rooms["Room 4"]["archr_mon_pos"]["c"] and r == rooms["Room 4"]["archr_mon_pos"]["r"] and rooms["Room 4"]["archr_monster"]:
                print(archr_monster_icon, end = "")
                c += 1 
            elif c == rooms["Room 6"]["archr_mon_pos"]["c"] and r == rooms["Room 6"]["archr_mon_pos"]["r"] and rooms["Room 6"]["archr_monster"]:
                print(archr_monster_icon, end = "")
                c += 1 
            elif c == rooms["Room 7"]["sword_mon_pos"]["c"] and r == rooms["Room 7"]["sword_mon_pos"]["r"] and rooms["Room 7"]["sword_monster"]:
                print(sword_monster_icon, end = "")  
                #c += 1 
            elif c == rooms["Room 10"]["apex_pred_pos"]["c"] and r == rooms["Room 10"]["apex_pred_pos"]["r"] and rooms["Room 10"]["apex_predator"]:
                print(apex_predator_icon, end = "")
            elif c == rooms["Room 10"]["sword_mon_pos"]["c"] and r == rooms["Room 10"]["sword_mon_pos"]["r"] and rooms["Room 10"]["sword_monster"]:
                print(sword_monster_icon, end = "")  
                c += 1
            else:
                print(rowString[c], end = "")
            c += 1
        r += 1
    
# ----------------------------------
# 📍 SHOW CURRENT ROOM
# ----------------------------------
def show_room(current_room):
    print(f"\n📍 You are in {current_room}.")
    print(rooms[current_room]["desc"])
    print(f"Your current score: {score}")

    # 👉 When you add items to rooms, you can show them here like this:
    if "item" in rooms[current_room]:
        if rooms[current_room]["item"] != "":
            print("👀 You have found a ", "".join(rooms[current_room]["item"]))
    else:
        print("No item here.")

# 🎒 Items collected will go here
def collect_item(current_room):
    if "item" in rooms[current_room]:
        inventory.append(rooms[current_room]["item"])
        print(f"10 points! for collecting the {rooms[current_room]['item']}")
        rooms[current_room]["desc"] = f"\nYou have collected the {rooms[current_room]['item']}."
        rooms[current_room]['item'] = "" # Remove the item from the room
        global score
        score += 10
        print(inventory)
    elif "item" in inventory:
        print("This item is already in your posession!")
        print(inventory)
    else:
        print("No item to collect in this room.")
        print(inventory)


# Use the items collected
def use_item(current_room):
    if current_room == "Room 2" and "⛏️ pickaxe" in inventory:
        global rocksfall
        rocksfall = False
        print(f"20 points! for removing the rocks from blocking the way.")
        rooms[current_room]["desc"] = "\nThe rocks have been removed, you can now move forward."
        global score
        score += 20
    else:
        print(f"Nothing happened.")



# Check inventory
def check_bag():
    if inventory == []:
        print("You have nothing in your bag.")
    else:
        print(f"You have {inventory} in your bag.")

# you die if you step on a trap or a fight a monster without a weapon, and you will be thrown back to start.
def death():
    global inventory
    inventory = []
    global score
    print(f"You have died. Final score: {score}")
    score = 0
    init_rooms()
    return "Room 1 - Start"

# ----------------------------------
# 🚶 MOVE BETWEEN ROOMS
# ----------------------------------
def move(direction, current_room):
    global inventory
    # Check if the direction exists in this room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        # Check if new room has a requirement, and if passages have traps and/or monsters.
        if "requires" in rooms[new_room] and rooms[new_room]["requires"] not in inventory:
            print(f"\n\t🔒 You need a {rooms[new_room]['requires']} to enter {new_room}!")
            return current_room # Stay in the current room
        elif (current_room == "Room 3" and direction == "forward") or (current_room == "Room 6" and direction == "backward"):
            print("Bad luck. You stepped on a plate and you were impaled in the chest by an arrow.")
            return death()
        elif (current_room == "Room 5" and direction == "forward") or (current_room == "Room 10" and direction == "backward"):
            print("Nice try. The bridge collapsed beneath you and you fell into the abyss.")
            return death()
        elif current_room == "Room 11 - Finish":
            print(rooms[current_room]["desc"])
            print(f"Your final score: {score}")
        else:
            print(f"\n🚶 You moved {direction} to {new_room}.")
            return new_room
    # If the direction is not valid
    else:
        print("\n⛔ You can't go that way!")
        return current_room


# ----------------------------------
# 🔁 MAIN GAME LOOP
# ----------------------------------
def game_loop():
    # Starting room
    current_room = "Room 1 - Start"
    show_intro()

    while True:
        if current_room == "Room 11 - Finish":
            print(rooms[current_room]["desc"])
            score += 100
            print(f"Your final score: {score}")
            save_game(current_room, inventory, score)
            play_again = input("Would you like to play again? ").strip().lower()
            if play_again == "no":
                print("👋 Thanks for playing!")
                break
            else:
                game_loop()

        show_room(current_room)
        
        # Ask the player for a command
        command = input("\n> ").strip().lower()

        # Movement commands
        if command in ("forward", "backward", "left", "right"):
            current_room = move(command, current_room)

        # Show help
        elif command == "help":
            show_help()
        
        # Show map
        elif command == "map":
            map(current_room)
        
        # Collect item
        elif command == "pick up":
            collect_item(current_room)
        
        # Use item
        elif command == "use":
            use_item(current_room)

        # Check inventory
        elif command == "inventory":
            check_bag()
        
        # Save game
        elif command == "save":
            save_game(current_room, inventory)

        # Load saved progress
        elif command == "load":
            loaded = load_game()
            current_room = loaded

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