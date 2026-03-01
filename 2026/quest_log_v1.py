# Quest Log
# PF 5.4
# Samuel Marriott 1/03/2026

def show_menu():
    #print("show_menu stub called")
    print("\n Quests Log Menu")
    print("Here are your options:")
    print("1: Add a quest")
    print("2: List your quests")
    print("3: Completed quests")
    print("4: Sort quests A-Z")
    print("5: Sort quests Z-A")
    print("6: Quit")

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
        for quest in quests:
            print(quest)

def complete_quest(quests):
    print("complete_quests stub")

def sort_quests_az(quests):
    print("sort_quest_az (A-Z) stub")

def sort_quests_za(quests):
    print("sort_quests_za (Z-A) stub")

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
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose 1-6.")


main()