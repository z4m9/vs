# Quest Log
# PF 5.3
# Samuel Marriott 1/03/2026

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
