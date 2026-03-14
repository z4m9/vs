# Program counts from 9 to 0
# Illustrating the functions of an IDE
for counter in range(9, 0, -1):
    if counter > 1:
        print("There were", counter, "green bottles sitting on the wall")
    else:
        print("There was 1 green bottle sitting on the wall")
print("and if the last green bottle should accidentally fall...")