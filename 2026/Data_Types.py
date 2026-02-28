# 1: assigns 7 + 2.2 = 9.2) to variable y
print() # Empty line for readability
y = 7 + 2.2
print ("1 ",y) 
print(type(y))

# 2: converts y from float to integer
print()
y = int(y)
print("2 ",y)
print(type(y))

# 3: converts y from integer to float
print()
y = float(y)
print("3 ",y)
print(type(y))

# 4: converts y from float to string
print()
y = str(y) # 
print("4 ",y)
print(type(y))

# 5: Converts y from string to float, then integer
print()
y = float(y)
y = int(y)
print("5 ",y)
print(type(y))