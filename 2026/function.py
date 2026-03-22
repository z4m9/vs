# Imperative
def squareSum(a, b):
    Sum = a + b
    Square = pow(Sum, 2)
    return Square

# Functional
def squareSum2(a, b):
    return pow(a + b, 2)

# Main
print(squareSum2(4, 5))

