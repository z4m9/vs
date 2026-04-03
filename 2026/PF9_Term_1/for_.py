# n a for loop is a standard convention indicating that the loop variable is not needed inside the loop body. It acts as a "throwaway" or dummy variable.

for _ in range(4):
    print(_)

my_list = [
    [" " for _ in range(3)] 
        for _ in range(3)
    ]
print(my_list)