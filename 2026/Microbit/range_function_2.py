from microbit import*
heart = "0x0x0:xxxxx:xxxxx:0xxx0:00x00"

def lights():
    display.show(Image(heart.replace('x', str(count))))
    sleep(200)
    
while True:
    for count in range(0, 10, 1):
        lights()

    for count in range(10, 0, -1):
        lights()