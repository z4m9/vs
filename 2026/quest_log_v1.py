# Quest Log
# PF 5.3
# Samuel Marriott 1/03/2026

def show_menu():
    print("Show_menu stub called")

def add_quest(quests):
    print("add_quest stub")

def list_quests(quests):
    print("list_quests stub")

def complete_quest(quests):
    print("complete_quest stub")

def sort_quests_az(quests):
    print("sort_quests_az stub")

def quests():
    print("quests declared")

def main():
    # TODO: Create an empty list called quests

    print("🧭 Welcome to Quest Log Manager (v1)")
    print("Type a menu option number to choose an action.")
    quests = ["Find the Lost Key", "Unlock the Ancient Gate", "Deliver the Secret Message"]
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
            sort_quests_az(quests)
        elif option == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose 1-6.")

main()
