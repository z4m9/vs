# Quest Log
# PF 5.4
# Samuel Marriott 1/03/2026

import random

def show_menu():
    #print("show_menu stub called")
    print("\n Quests Log Menu")
    print("Here are your options:")
    print("1: Add a quest")
    print("2: List your quests")
    print("3: Completed quests")
    print("4: Sort quests A-Z")
    print("5: Sort quests Z-A")
    print("6: Suggest random quest")
    print("7: Quit")

def add_quest(quests):
    #print("add_quest stub") # Temporary
    quest = input("Enter quest name here: ")
    quests.append(quest)
    print(f"Quest added confirmed: {quest}")

def list_quests(quests):
    #print("list_quests stub") # Temporary
    len(quests)
    if quests == []:
        print("No quests yet")
    else:
        i = 0
        for quest in quests:
            print(i,". ", quest)
            i += 1

def complete_quest(quests):
    #print("complete_quests stub")
    list_quests(quests)
    item = int(input("Which quest has been completed and can be removed? "))
    quests.pop(item)
    print(f"Quest confirmed removed: {item}")
    list_quests(quests)

def sort_quests_az(quests):
    #print("sort_quest_az (A-Z) stub")
    quests.sort()
    print(quests)
    print("List sorted alphabetically confirmed")

def sort_quests_za(quests):
    #print("sort_quests_za (Z-A) stub")
    quests.sort(reverse = True)
    print(quests)
    print("List was reverse sorted.")

def suggest_random_quest(quests):
    if len(quests) == []:
        print("No quests to choose from.")
    else:
        random_quest = random.choice(quests)
        print(random_quest)

def main():
    # TODO: Create an empty list called quests
    quests = []
    print("🧭 Welcome to Quest Log Manager (v1)")
    print("Type a menu option number to choose an action.")

    while True:
        show_menu()
        option = input("Choose an option (1-6): ").strip()

        if option == "1":
            add_quest(quests)
        elif option == "2":
            list_quests(quests)
        elif option == "3":
            complete_quest(quests)
        elif option == "4":
            sort_quests_az(quests)
        elif option == "5":
            sort_quests_za(quests)
        elif option == "6":
            suggest_random_quest(quests)
        elif option == "7":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose 1-6.")

main()