# Quest Log Version 2
# Samuel Marriott 2/03/2026
# PF 5.4

def show_menu():
    print("\n Quest Log v2")
    print("1: Add quest")
    print("2: List quests")
    print("3: Quit")

def add_quest(quests):
    # TODO: Add a quest as [name, points]
    name = input("Enter quest name: ").strip()
    points = int(input("Enter the score value: "))
    quests.append([name, points])
    print(quests)

def list_quests(quests):
    # TODO: Display quests in numbered format
    r = 0 # row
    c = 0 # column
    while r < len(quests):
        print(r + 1, ". ", quests[r][c], " - ", quests[r][c + 1], " points")
        r += 1
        #c += 1

def main():
    quests = []   # This will now store [name, points]

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_quest(quests)
        elif choice == "2":
            list_quests(quests)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()