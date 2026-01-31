# Samuel Marriott's code 14/4/2025
import pygame
from pygame.locals import *
import json
pygame.init()
import random
import time
import sys

# Declare globalled variables
WIDTH = 1000
HEIGHT = 600
bluefade = 150                          # blue background fade vale
blueforward = True                      # blue background fade direction
platcolour = 0, 0, 139                  # platforms colour
ninja = Actor('jumper-1', (500, 250))   # Ninja player
ninja_x_velocity = 0
ninja_y_velocity = 0
gravity = 1
respawn = 0
jumping = False
jumped = False
allowx = True
timer = []
lives = 5                               # Player Lives remaining counter
splash = 500                            # Splash screen time counter
endgame = 300                           # Game quits automatically when its finished

# Platforms
floor = Rect((0, HEIGHT-20), (WIDTH, 20))      # The ground platform
P61left = True
P62left = False
P1 = Rect((450, 500), (100, 10))        # creates platform - middle of screen
P2 = Rect((300, 400), (100, 10))        # ...moving out left
P3 = Rect((600, 400), (100, 10))        # ...moving out right
P4 = Rect((200, 300), (100, 10))        # ...moving out left
P5 = Rect((700, 300), (100, 10))        # ...moving out right
P6 = Rect((100, 200), (100, 10))        # ...moving out left
plat61_x = 200
plat62_x = 700
P61 = Rect((plat61_x, 200), (100, 10))  # variable platforms
P62 = Rect((plat62_x, 200), (100, 10))
P7 = Rect((800, 200), (100, 10))        # ...moving out right
P8 = Rect((0, 100), (100, 10))          # top far left
P9 = Rect((900, 100), (100, 10))        # top far right
platforms = [floor, P1, P2, P3, P4, P5, P6, P7, P8, P9, P61, P62] # List of platforms and ground

# Gems
diamond_x = [950, 50, 850, 150, 750, 250, 650, 350, 500]
diamond_y = [70, 70, 170, 170, 270, 270, 370, 370, 470]
d_xy = random.randint(0, 8)
gem = Actor('diamond_s', (diamond_x[d_xy], diamond_y[d_xy]))
points = 0

# Fruits
cherry_x = [950, 50, 850, 150, 750, 250, 650, 350, 500]
cherry_y = [70, 70, 170, 170, 270, 270, 370, 370, 470]
c_xy = random.randint(0, 8)
fruit = Actor('cherry_s', (cherry_x[c_xy], cherry_y[c_xy]))

High_score = 0
def getscore():                        # Load the high scores from Json file
    global High_score
    Highest_score = "none"
    try:
        with open('High_scores.json') as file:
            data = json.load(file)
            file.close()               # load file
        for i in data['Scores']:
            High_score = int(i['Score'])
            #print("High score testing:", High_score) - debugger
            Highest_score = i['Name'] +': '+ str(i['Score'])
    except:
        print("Error 2")
    return Highest_score

Highest_score = getscore()
is_new_high_score = False

def savescore():
    global High_score
    High_score = points
    winner = "Samuel"
    data = {"Scores":[{"Name": winner,"Score": High_score}]}
    try:
        f = open('High_scores.json', 'w')
        json.dump(data, f)
        f.close()
    except:
        print("Error 1")

# Music
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
sounds.ninja_music.play(-1)

def draw():
    global P61, P62, splash, is_new_high_score, endgame
    splash -= 1
    screen.fill((173, 216, bluefade))
    if splash > 0:                                      # show the splash creen for a few seconds
        screen.blit('ninja_ai', (0, 0))
        screen.draw.text("Welcome to Ninja Jumper", center = (500, 300), fontsize = 100, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
        screen.draw.text("High score:", center = (450, 370), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
        screen.draw.text(Highest_score, center = (650, 370), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
        screen.draw.text("Collect gems and fruits by making the", topleft = (150, 100), fontsize = 40, shadow = (1, 1), color = (0, 255, 0), scolor = "#202020", align="left")
        screen.draw.text("ninja jump between platforms without dying.", topleft = (150, 140), fontsize = 40, shadow = (1, 1), color = (0, 255, 0), scolor = "#202020", align="left")
        screen.draw.text("Controls are up arrow for jump,", topleft = (150, 180), fontsize = 40, shadow = (1, 1), color = (0, 255, 0), scolor = "#202020", align="left")
        screen.draw.text("left and right arrows for moving around.", topleft = (150, 220), fontsize = 40, shadow = (1, 1), color = (0, 255, 0), scolor = "#202020", align="left")
    elif lives > 0:                                     # NINJA IS ALIVE
        screen.blit('skyline_construction3', (0, 0))    # Background is drawn
        P61 = Rect((plat61_x, 200), (100, 10))          # Moving platforms
        P62 = Rect((plat62_x, 200), (100, 10))          # Moving platforms
        platforms[10] = P61
        platforms[11] = P62
        for i in platforms:                             # Drawing the platforms and ground
            screen.draw.filled_rect(i, platcolour)
        ninja.draw()                                    # Drawing the ninja
        gem.draw()                                      # Drawing the gems
        fruit.draw()                                    # Drawing the fruit
        screen.draw.text("Score:", topleft = (50, 440), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020", align = "left")
        screen.draw.text(str(points), topleft = (45, 470), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020", align = "left")
        screen.draw.text("Lives:", center = (50, 340), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
        screen.draw.text(str(lives), center = (45, 370), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
    else:
        #print("Ninja has died")          # debug and testing THE NINJA DEATH
        if points > int(High_score):
            savescore()
            is_new_high_score = True
            #print('high score was saved') # debug and testing high score achievement
        screen.blit('skyline_large', (0, 0))
        gem.draw()
        fruit.draw()
        P61 = Rect((plat61_x, 200), (100, 10))
        P62 = Rect((plat62_x, 200), (100, 10))
        platforms[10] = P61
        platforms[11] = P62
        for i in platforms:
            screen.draw.filled_rect(i, platcolour)
        ninja.image = 'jumper-splat'
        ninja.draw()
        timer = []
        if is_new_high_score == True:
            screen.draw.text("New high score: "+str(High_score), center = (300, 100), fontsize = 60, shadow = (1, 1), color = (0, 255, 0), scolor = "#202020")
            print('new high score test it is shown on the screen')
        screen.draw.text("GAME OVER!", center = (500, 300), fontsize = 100, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
        sounds.ninja_music.stop()
        endgame -= 1
        if endgame < 1:
            pygame.quit()
            sys.exit()

def update():
    if lives > 0:
        backgroundcolourfade()
        platform_mover()
        ninja_move()

def ninja_move():
    global ninja_x_velocity, ninja_y_velocity, jumping, gravity, jumped, allowx, timer, points, d_xy, c_xy, lives, respawn, splash
    if respawn < 1:
        if ninja_x_velocity == 0 and not jumped:
            ninja.image = 'jumper-1'                # Ninja is facing the front

        if collidecheck():                          # gravity
            gravity = 1                             # rate of falling
            ninja.y -= 1
            allowx = True
            timer = []
        if not collidecheck():
            ninja.y += gravity                      # falling down
            if gravity <= 20:                       # slower fall
                gravity += 0.5
            timer.append(pygame.time.get_ticks())
            if len(timer) > 5 and not jumped:
                allowx = False
                ninja.image = 'jumper-up'
                if len(timer) > 20:
                    ninja.image = 'jumper-fall'
                    if len(timer) > 30:
                        ninja.image = 'jumper-fall2' # more wind, falling faster
                        #print('{(timer gt 30)}')
                        if len(timer) > 35 and ninja.y > 550 and ninja.colliderect(floor):
                            ninja.image = 'jumper-splat'
                            respawn = 100
                            lives -= 1               # Decrementing the lives remaining
                            timer = []
                            sounds.grunt_1.play()

        if (keyboard.left) and allowx:
            if (ninja.x > 40) and (ninja_x_velocity > -8):
                ninja_x_velocity -= 2
                ninja.image = "jumper-left"
                if (keyboard.left) and jumped:
                    ninja.image = "jumper-jleft"    # left movement
        if (keyboard.right) and allowx:
            if (ninja.x < 960) and (ninja_x_velocity < 8):
                ninja_x_velocity += 2
                ninja.image = "jumper-right"
                if (keyboard.right) and jumped:
                    ninja.image = "jumper-jright"       # Right movement

        ninja.x += ninja_x_velocity

        if ninja_x_velocity > 0:                        # velocity
            ninja_x_velocity -= 1
        if ninja_x_velocity < 0:
            ninja_x_velocity += 1
        if ninja.x < 50 or ninja.x > 950:               # Edge of screen on x axis
            ninja_x_velocity = 0

        if (keyboard.up) and collidecheck() and not jumped:
            sounds.jump.play()
            jumping = True
            jumped = True
            clock.schedule_unique (jumpedrecently, 0.4)      # jump delay
            ninja.image = "jumper-up"
            ninja_y_velocity = 95                            # jumping
        if jumping and ninja_y_velocity > 25:
            ninja_y_velocity -= ((100 - ninja_y_velocity)/2) # slowing down the jump
            ninja.y -= ninja_y_velocity/3                    # jump height
        else:
            ninja_y_velocity = 0
            jumping = False
    else:
        respawn -= 1
        ninja.image = 'jumper-splat'

    if ninja.colliderect(gem):               # Gem collision
        points += 1                          # Gem points awarded
        sounds.gem.play()
        old_d_xy = d_xy
        d_xy = random.randint (0, 8)
        while old_d_xy == d_xy:
            d_xy = random.randint (0, 8)
        gem.x = diamond_x[d_xy]
        gem.y = diamond_y[d_xy]

    if ninja.colliderect(fruit):                # Fruit collision
        points += 2                             # Fruit points awarded
        sounds.gem.play()
        old_c_xy = c_xy
        c_xy = random.randint (0, 8)
        while old_c_xy == c_xy:
            c_xy = random.randint (0, 8)
        fruit.x = cherry_x[c_xy]
        fruit.y = cherry_y[c_xy]

def platform_mover():                          # Moving platforms
    global plat61_x, plat62_x, P61left, P62left
    if P61left:                                # left platform
        plat61_x += 2
        if plat61_x == 400:
            P61left = False
        if ninja.colliderect(P61):
            ninja.x += 2
    else:
        plat61_x -= 2
        if plat61_x == 200:
            P61left = True
        if ninja.colliderect(P61):
            ninja.x -= 2
    if P62left:                                 # right platform
        plat62_x += 2
        if plat62_x == 700:
            P62left = False
        if ninja.colliderect(P62):
            ninja.x += 2
    else:
        plat62_x -= 2
        if plat62_x == 500:
            P62left = True
        if ninja.colliderect(P62):
            ninja.x -= 2

def collidecheck():                 # Item colliding
    collide = False
    for i in platforms:
        if ninja.colliderect(i):
            collide = True
    return collide

def jumpedrecently():               # Jumping
    global jumped
    jumped = False

def backgroundcolourfade():         # background colour changing
    global bluefade, blueforward
    if bluefade < 255 and blueforward:
        bluefade += 1
    else:
        blueforward = False
    if bluefade > 130 and not blueforward:
        bluefade -= 1
    else:
        blueforward = True
# End of code.
