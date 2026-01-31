# https://pygame-zero.readthedocs.io/en/stable/introduction.html
# https://www.pygame.org/docs/ref/examples.html?highlight=actor
# Importing the pygame module
import pygame
import pgzrun
import random
#import time
WIDTH = 800
HEIGHT = 600
# HEIGHT = alien.height + 20
blue=150
red=(255,0,0)
green=(0, 255, 0)
blue1 = (0,0,255)
dblue = (0,0,128)
lblue=(0, 128, 255)
yellow=(255, 255, 0)
dgreen=(10, 200, 0)
lgreen=(0, 255, 150)

xy=chr(228) 

alien = Actor('diamond_s')
alien.pos = 100, 56

blueforward = True
groundcolour = (0,0,blue)
floor = Rect((0,HEIGHT-10), (WIDTH,10))


# Ninja
ninja = Actor('jumper-fall', (500,250))
ninja.pos = 200,60
ninja_x_velocity = 0
ninja_y_velocity = 0
gravity = 1
death=0
jumping = False
jumped = False
allowx = True
timer = []

P61left = True
P62left = False
P1 = Rect((450, 500), (100, 10)) # creates platform - middle of screen
P2 = Rect((300, 400), (100, 10)) # ...moving out left
P3 = Rect((600, 400), (100, 10)) # ...moving out right
P4 = Rect((200, 300), (100, 10)) # ...moving out left
P5 = Rect((700, 300), (100, 10)) # ...moving out right
P6 = Rect((100, 200), (100, 10)) # ...moving out left
plat61_x = 200
plat62_x = 700
P61 = Rect((plat61_x, 200), (100, 10))
P62 = Rect((plat62_x, 200), (100, 10))
P7 = Rect((800, 200), (100, 10)) # ...moving out right
P8 = Rect((0, 100), (100, 10)) # top far left
P9 = Rect((900, 100), (100, 10)) # top far right
platforms = [floor, P1, P2, P3, P4, P5, P6, P7, P8, P9, P61, P62]

# Gems
diamond_x = [950, 50, 850, 150, 750, 250, 650, 350, 500]
diamond_y = [70, 70, 170, 170, 270, 270, 370, 370, 470]
d_xy = random.randint(0, 8)
gem = Actor('diamond_s', (diamond_x[d_xy], diamond_y[d_xy]))
points = 0
lives=3

# Music
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
#sounds.ninja_music.play(-1)

def draw():
	#  global P61, P62
    screen.fill(lblue)
    screen.blit('skyline_large', (0, 0))
    P61 = Rect((plat61_x, 200), (100, 10))
    P62 = Rect((plat62_x, 200), (100, 10))
    platforms[10] = P61
    platforms[11] = P62
    for i in platforms:
        screen.draw.filled_rect(i, red)
    ninja.draw()
    gem.draw()
    alien.draw()
	
    screen.draw.text("Loot:", center = (50, 440), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
    screen.draw.text(str(points), center = (45, 470), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
    screen.draw.text("Lives:", center = (50, 340), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")
    screen.draw.text(str(lives), center = (45, 370), fontsize = 40, shadow = (1, 1), color = (255, 255, 255), scolor = "#202020")

def update():
    backgroundcolourfade()
    platform_mover()
    ninja_move()

def ninja_move():
    global ninja_x_velocity, ninja_y_velocity, jumping, gravity, jumped, allowx, timer, points, d_xy, death, lives
    if death < 1:
            
        # facing the front
        if ninja_x_velocity == 0 and not jumped:
            ninja.image = 'jumper-1'

        # gravity
        if collidecheck():
            gravity = 1
            ninja.y -= 1
            allowx = True
            timer = []
        if not collidecheck():
            ninja.y += gravity
            if gravity <= 20:
                gravity += 0.5
            timer.append(pygame.time.get_ticks())
            if len(timer) > 5 and not jumped:
                allowx = False
                ninja.image = 'jumper-up'
                if len(timer) > 20:
                    ninja.image = 'jumper-fall'
                    if len(timer) > 30:
                        ninja.image = 'jumper-fall2'
                        if len(timer) > 35 and ninja.y > 550 and ninja.colliderect(floor):
                            ninja.image = 'jumper-splat'
                            death = 100
                            lives -=1
                            timer=[]
                            

        # left and right movement
        if (keyboard.left) and allowx:
            if (ninja.x > 40) and (ninja_x_velocity > -8):
                ninja_x_velocity -= 2
                ninja.image = "jumper-left"
                if (keyboard.left) and jumped:
                    ninja.image = "jumper-jleft"
        if (keyboard.right) and allowx:
            if (ninja.x < 960) and (ninja_x_velocity < 8):
                ninja_x_velocity += 2
                ninja.image = "jumper-right"
                if (keyboard.right) and jumped:
                    ninja.image = "jumper-jright"

        ninja.x += ninja_x_velocity
    # print(allowx)
        # velocity
        if ninja_x_velocity > 0:
            ninja_x_velocity -= 1
        if ninja_x_velocity < 0:
            ninja_x_velocity += 1
        if ninja.x < 50 or ninja.x > 950:
            ninja_x_velocity = 0

        # jumping
        if (keyboard.up) and collidecheck() and not jumped:
            sounds.jump.play()
            jumping = True
            jumped = True
            clock.schedule_unique (jumpedrecently, 0.4) # jump delay
            ninja.image = "jumper-up"
            ninja_y_velocity = 95
        if jumping and ninja_y_velocity > 25:
            ninja_y_velocity = ninja_y_velocity - ((100 - ninja_y_velocity)/2)
            ninja.y -= ninja_y_velocity/3 # jump height
        else:
            ninja_y_velocity = 0
            jumping = False

        # Gem collision
        if ninja.colliderect(gem):
            points += 1
            sounds.gem.play()
            old_d_xy = d_xy
            d_xy = random.randint (0, 8)
            while old_d_xy == d_xy:
                d_xy = random.randint (0, 8)
            gem.x = diamond_x[d_xy]
            gem.y = diamond_x[d_xy]

    else:
        death -=1
        
        
        
    print(ninja_x_velocity, ninja_y_velocity, ninja.y, death, timer)


def platform_mover():
    global plat61_x, plat62_x, P61left, P62left
    # left platform
    if P61left:
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
    # right platform
    if P62left:
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
    #print(plat62_x)

def collidecheck():
    collide = False
    for i in platforms:
        if ninja.colliderect(i):
            collide = True
    return collide

def jumpedrecently():
    global jumped
    jumped = False

def backgroundcolourfade():
    global blue, blueforward
    if blue < 255 and blueforward:
        blue += 1
    else:
        blueforward = False
    if blue > 130 and not blueforward:
        blue -= 1
    else:
        blueforward = True





pgzrun.go()