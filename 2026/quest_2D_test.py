# quest 2D test
# PF 5.4
# Samuel Marriott 1/03/2026

quests = [
    ["Find Key", 10],
    ["Repair Bridge", 20],
    ["Unlock Gate", 15]
]

print("First quest name:", quests[0][0])
print("Points for second quest:", quests[1][1])
# 1
print()
for quest in quests:
    print(f"{quest[0]} — {quest[1]} points")
# 2
print()
for i in range(len(quests)):
    print(f"{i + 1}. {quests[i][0]} — {quests[i][1]} points")
# Spot a difference?