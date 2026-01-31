# debug how to get user input
import pygame									# Importing the pygame module
import pgzrun
#from pygame.locals import *
#pygame.init()									# Initiate to give permission to use pygame's functionality

dblue = (0,0,128)
lblue=(0, 128, 255)
dgreen = (0,255,128)
lgreen=(0, 255, 255)
lred=(255, 30, 30)
brown=(100, 30, 30)
cursor=(20,20,20)

window = pygame.display.set_mode((600, 600))	# display surface object of specific dimension
window.fill(brown) 						# Filling the window with color

clock = pygame.time.Clock()						# Create a new clock object to track the amount of time
player1 = Rect(400, 500, 50, 50)				# Create a new rect for first object
player2 = Rect(400, 0, 50, 50)					# Create a new rect for second object
input_box = Rect(100, 100, 140, 32)
gravity = 1     								# Creating variable for gravity
font = pygame.font.SysFont(None, 30)
text = ''
active = False
run = True								# boolean variable used to run the while loop

def getKey():   # get the key strokes the user types
    global active, text, run, cursor
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quit ',active)
            run = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse click',active)
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            cursor = lred if active else lgreen
        if event.type == pygame.KEYDOWN:
            print('key ',active)
        #if active:
            if event.key == pygame.K_RETURN:
                print(text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode


def getInput():         # draw a input box for user to enter text
    getKey()
    txt_surface = font.render(text, True, cursor)
    width = max(120, txt_surface.get_width() + 10)
    input_box.w = width
    window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(window, dblue, input_box, 2)
    

while run:								# Creating an infinite loop to run our game
	clock.tick(20)						# Set the framerate to (typically 60fps)
	getInput()
	player2.bottom += gravity			# Adding gravity in player2

	collide = pygame.Rect.colliderect(player1, player2) # Checke if player is colliding with platform or not using the colliderect() method. It will return a boolean value
	if collide:											# If the objects are colliding then changing the y coordinate
		player2.bottom = player1.top
		run=False

	
	pygame.draw.rect(window, (0, 255, 0),player1)		# Drawing player 1 rect
	pygame.draw.rect(window, (0, 0, 255),player2)		# Drawing player 2 rect
	pygame.display.update()								# Updating the display surface
	
if run==False:
    print('quit the game')
    pygame.quit()

pgzrun.go()