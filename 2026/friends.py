# friends
# PF 5.2
# Samuel Marriott 1/03/2026
# Refer to List Processing
friends = ["Alex", "Sam", "Jordan"] # From 5.2 instructions

print(f"Original list: {friends}")
friends.append("Harry") # Step 1
friends.append("Roger")
#print(friends) # Test
friends.remove("Alex") # Step 2
#print(friends) # Test
friends.pop(1) # Step 3
#print(friends) # Test
friends.append("Cameron") # Step 4
friends.append("Phil")
#print(friends) # Test
friends.sort()
print(f"New list: {friends}")
print(f"Number of friends: {len(friends)}") # Step 5

for friend in friends: # Step 6 (for)
    print(friend)
n = 0
while n < 5: # Step 6 (while)
    print(friends[n])
    n += 1