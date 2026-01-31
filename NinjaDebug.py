# Write your code here :-)
import time
import pygame
import random
WIDTH = 1000
HEIGHT = 600

blue = 150
blueforward = True
groundcolour = 0,0,139
floor = Rect ((0,580),(1000,20))
#Ninja
ninja = Actor('jumper-1',(500,250))
ninja_x_velocity = 0
ninja_y_velocity = 0
gravity = 1
jumping = False
jumped = False
allow_x = True
points = 0
timer = []

#platforms
platform1 = Rect((450,500),(100,10)) #creates platform - middle of screen
platform2 = Rect((300,400),(100,10))
platform3 = Rect((600,400),(100,10))
platform4 = Rect((200,300),(100,10))
platform5 = Rect((700,300),(100,10))
platform6 = Rect((100,200),(100,10))
platform61_x = 200
platform62_x = 700
platform61 = Rect((platform61_x,200),(100,10))
platform62 = Rect((platform62_x,200),(100,10))
platform7 = Rect((800,200),(100,10))
platform8 = Rect((0,100),(100,10))
platform9 = Rect((900,100),(100,10))
platforms = [floor,platform1,platform2,platform3,platform4,platform5,platform6,platform61,platform62,platform7,platform8,platform9] #list

#game speed 60times/second

platform61left = True
platform62left = False

#Gems
diamond_x = [950,50,850,150,750,250,650,350,500]
diamond_y = [70,70,170,170,270,270,370,370,470]
random_xy = random.randint(0,8)
gem = Actor('diamond_s', (diamond_x[random_xy], diamond_y[random_xy]))

#music
#pygame.mixer.pre_init(22050, -16, 2, 1024)
#pygame.init()
#pygame.mixer.quit()
#pygame.mixer.init(22050, - 16, 2, 1024)
#sounds.ninja_music.play(-1)


def draw():
    global platform61, platform62
    screen.fill((173,216,blue))
    screen.blit('skyline_large',(0,0))
    platform61 = Rect((platform61_x,200),(100,10))
    platform62 = Rect((platform62_x,200),(100,10))
    platforms[7] = platform61
    platforms[8] = platform62
    for i in platforms:
        screen.draw.filled_rect(i,groundcolour)
    ninja.draw()
    gem.draw()
    screen.draw.text("Loot", center=(50,540),fontname = 'mini_square', fontsize = 40, shadow = (1,1), color = (255,255,255), scolor = "#202020")
    screen.draw.text(str(points), center=(45,570), fontsize = 40, shadow = (1,1), color = (255,255,255), scolor = "#202020")

def update():
    backgroundcolourfade()
    platform_mover()
    ninja_move()

def ninja_move():
    global ninja_x_velocity, ninja_y_velocity, gravity, jumping, jumped, allow_x, timer, points, random_xy

    #facing the front
    if ninja_x_velocity == 0 and jumped == False:
        ninja.image = 'jumper-1'

    #gravity
    if collidecheck():
        gravity = 1
        ninja.y -= 1
        allow_x = True
        timer = []
    if not collidecheck():
        ninja.y += gravity
        if gravity <= 20:
            gravity += 0.5
        timer.append(pygame.time.get_ticks())
        if len(timer) > 5 and jumped == False:
            allow_x = False
            ninja.image = 'jumper-up'
            if len(timer) > 20:
                ninja.image = 'jumper-fall'
                if len(timer) > 30:
                    ninja.image = 'jumper-fall2'
    #left and right section
    if (keyboard.a) and allow_x == True:
        if (ninja.x >40) and (ninja_x_velocity > -8):
            ninja_x_velocity -= 2
            ninja.image = 'jumper-left'
            if (keyboard.a) and jumped:
                ninja.image = 'jumper-jleft'
    if (keyboard.d) and allow_x == True:
        if (ninja.x <960) and (ninja_x_velocity < 8):
            ninja_x_velocity += 2
            ninja.image = 'jumper-right'
            if (keyboard.d) and jumped:
                ninja.image = 'jumper-jright'

    ninja.x += ninja_x_velocity
    #velocity section
    if ninja_x_velocity > 0:
        ninja_x_velocity -= 1
    if ninja_x_velocity < 0:
        ninja_x_velocity += 1
    if ninja.x <50 or ninja.x > 950:
        ninja_x_velocity = 0
    #jumping
    if (keyboard.w) and collidecheck() and jumped == False:
        sounds.jump.play()
        jumping = True
        jumped = True
        clock.schedule_unique(jumpedrecently,0.4)
        ninja.image = 'jumper-up'
        ninja_y_velocity = 95
    if jumping and ninja_y_velocity > 25:
        ninja_y_velocity = ninja_y_velocity - ((100 - ninja_y_velocity)/2)
        ninja.y -= ninja_y_velocity/3 #jump height
    else:
        ninja_y_velocity = 0
        jumping = False
#Gem collision

    if ninja.colliderect(gem):
        points += 1
        sounds.gem.play()
        old_random_xy = random_xy
        random_xy = random.randint(0,8)
        while old_random_xy == random_xy:
            random_xy = random.randint(0,8)
        gem.x = diamond_x[random_xy]
        gem.y = diamond_y[random_xy]


def platform_mover():
    global platform61_x, platform62_x, platform61left, platform62left
    #left platform
    if platform61left:
        platform61_x += 2
        if platform61_x == 400:
            platform61left = False
        if ninja.colliderect(platform61):
            ninja.x += 2
    else:
        platform61_x -= 2
        if platform61_x == 200:
            platform61left = True
        if ninja.colliderect(platform61):
            ninja.x -= 2
    #right platform
    if platform62left:
        platform62_x += 2
        if platform62_x == 700:
            platform62left = False
        if ninja.colliderect(platform62):
            ninja.x += 2
    else:
        platform62_x -= 2
        if platform62_x == 500:
            platform62left = True
        if ninja.colliderect(platform62):
            ninja.x -= 2

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
