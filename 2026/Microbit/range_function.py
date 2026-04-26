# Imports go at the top
# Samuel Marriott 26/04/2026 1.12 MECH Activity 2.
# DO NOT RUN CODE HERE! If you wish to run the code, open the microbit python editor and copy & paste the code there.
from microbit import *

# Code in a 'while True:' loop repeats forever
heart = "0x0x0:xxxxx:xxxxx:0xxx0:00x00"

while True:
    # Swap x's for string of 9's
    heart_now = heart.replace('x', str(9))
    display.show(Image(heart_now))
    sleep(500)
    # Swap x's for string of 0's
    heart_now = heart.replace('x', str(0))
    display.show(Image(heart_now))
    sleep(500)