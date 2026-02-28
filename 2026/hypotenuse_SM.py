# hyoptenue_SM 
# PF3
# Sam M 22-Feb-2026

import math
a = int(input("State the length of side a of your right-angled triangle: "))
b = int(input("State the length of side b of your right-angled triangle: "))
c = math.sqrt(a**2 + b**2) # Square root the square of a and b
c_rounded = round(c, 1) # Round to one decimal place
print(c_rounded) # Final result
