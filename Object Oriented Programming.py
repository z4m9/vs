# Ask for name
def greet():
    name = input("What is your name? ")
    print("Hi", name)

# Times tables
def times_table(number):
    print(number, "times table")
    for i in range (10):
        print(str(number * i))

# Put it together
greet()
times_table()