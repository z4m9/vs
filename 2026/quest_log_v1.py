# Quest Log
# PF 5.3
# Samuel Marriott 1/03/2026

# multi line comment 
"""
1️⃣ add_quest(quests) — Add a new quest

Ask the user to enter a quest 
Add to the quests array using append()
Print a confirmation message
✅ Extensions

Use .strip() method so extra spaces don’t affect the input.
Check the input is not empty ("").
Use the in operator to prevent duplicates.
2️⃣ list_quests(quests) — Display all quests

Use len() to check if the list is empty. If it is, display a message such as “No quests yet.” Otherwise, use a loop to display each quest on a new line.

✅ Extensions

Display the quests with numbers (1, 2, 3…) so it matches how you will select quests in complete_quest().
Display the total count: “You have X active quests.”
3️⃣complete_quest(quests) — Complete (remove) a quest
If the list is empty, display a message and return to the menu. Otherwise, display the quests with numbers (1, 2, 3…), then ask the user which quest number to complete, remove the correct quest from the list, and confirm which quest was removed.

✅ Extensions (recommended)

Input validation: if the user types something that isn’t a number, display an error message and return to the menu.
Range check: if the user enters 0 or a number larger than the list length, display an error message and return to the menu.
Index conversion: remember list indexes start at 0, so quest number 1 corresponds to index 0.
Empty list handling: after removing, optionally show the updated number of quests remaining.
(Optional extra): Allow the user to type cancel instead of a number to return to the menu.

4️⃣ sort_quests_az(quests) — Sort A–Z

Sort the list using sort() and print a short confirmation message.

✅ Extensions

If the list is empty, print “No quests to sort.”
5️⃣ sort_quests_za(quests) — Sort Z–A

Sort the list using sort(reverse=True) and print a short confirmation message.

✅ Extension

If the list is empty, print “No quests to sort.”
🎲 Generating Random Numbers
Many programs require some level of randomness. For example rolling a dice, triggering a random event in an adventure game, or selecting a random question from a quiz.

Computers do not generate true randomness. Instead, they use mathematical formulas to generate pseudo-random numbers — values that appear random but are produced by an algorithm.

In Python, random numbers are generated using the random module. Before using it, the module must be imported at the top of the program:

import random
Python provides several useful functions, including:

random.randint(a, b) → returns a random integer between a and b (inclusive)
random.choice(list) → selects a random item from a list
For example:

import random

numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))
 Each time the program runs, a different value may be selected.

💻Activity — Generating Random Quests
Create a function to  quest_log_v1.py to suggest and display a random quest — def suggest_random_quest(quests):
Adjust the numbering so Quit remains as the last option.
Reuse some of your previous code to check if the list is empty.
Otherwise, use random.choice(quests) to display a randomly selected quest.
Update your menu options and show_menu() to include this new feature.
Run the program multiple times to test this function. You will be asked to upload screenshots of the output and the .pyfile later in this lesson.
"""



def show_menu():
    print("\n Quests Log Menu")
    print("Here are your options:")
    print("1: Find the Lost Key")
    print("2: Unlock the Ancient Gate")
    print("3: Deliver the Secret Message")
    print("4: Complete the Obstance Course")
    print("5: Defeat the Boss")
    print("6: Quit")

def add_quest(quests):
    quest = input("Enter your quest: ")
    quests.append(quest)
    print(f"Quest confirmed: {quest}")
    print(quests)
    print("Enjoy your time.")

def list_quests(quests):
    len(quests)
    if quests == []:
        print("No quests yet")
    else:
        print(f"Your quests: {quests}")

def complete_quest(quests):
    print("complete_quest stub")

def sort_quests_az(quests):
    print("sort_quests_az stub")

def sort_quests_za(quests):
    print("sort_quests_az stub")

def quests():
    print("quests declared")

def main():

    print("🧭 Welcome to Quest Log Manager (v1)")
    print("Type a menu option number to choose an action.")
    # An empty list called quests
    quests = []
    while True:
        user = input("Would you like to complete a quest of your own? ")
        if user == "Yes":
            add_quest(quests)
        else:
            list_check = input("Do you want to check your quest list? ")
            if list_check == "Yes":
                list_quests(quests)
            else:
                show_menu()
        option = input("Choose an option (1-6): ").strip()
        if option == "1":
            print("Your selected quest: Find the Lost Key")
        elif option == "2":
            print("Your selected quest: Unlock the Ancient Gate")
            list_quests(quests)
        elif option == "3":
            print("Your selected quest: Deliver the Secret Message")
            complete_quest(quests)
        elif option == "4":
            print("Your selected quest: Complete the Obstance Course")
            sort_quests_az(quests)
        elif option == "5":
            print("Your selected quest: Defeat the Boss")
            sort_quests_za(quests)
        elif option == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose 1-6.")

main()
