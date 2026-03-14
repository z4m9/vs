# Error Types
# Created by Samuel Marriott on 15/03/2026

def add_ten():
    x = int(input("Enter a number: "))
    y = x
    y += 10  
    print(f'10 more is {y}'.format(x))

add_ten()

# Description of errors initially in code:
'''1. Initial syntax errors:
    - Line 5: Initially missing an end quote.
    - Line 4: Missing colon after add_ten().
    - Line 5: Needed to be indented.
    - Line 8: Missing a close bracket.'''
'''2. Initial runtime errors:
    - Line 5: Missing an int() function'''
'''3. Initial logic errors:
    - Inputted an example number (30)
    - Line 8: Expected output: "10 more is 40". Instead I got "10 more is 30"
        Error: Required f string with y inside {}'''