# debug how to use pygame in vs code
import pygame									# Importing the pygame module
import pgzrun
#from pygame.locals import *
#pygame.init()									# Initiate to give permission to use pygame's functionality
window = pygame.display.set_mode((600, 600))	# display surface object of specific dimension
window.fill((255, 255, 255)) 						# Filling the window with white color

clock = pygame.time.Clock()						# Create a new clock object to track the amount of time
player1 = Rect(200, 500, 50, 50)				# Create a new rect for first object
player2 = Rect(200, 0, 50, 50)					# Create a new rect for second object
gColour = 0,0,139								# Ground colour
floor = Rect((0,580), (1000,20))				# floor of the playing surface
ninja = Actor('jumper-1', (500,250))
gravity = 4										# Creating variable for gravity

def draw2():
    #screen.clear()
    window.blit('jumper-1', (500, 250))

run = True								# boolean variable used to run the while loop
while run:								# Creating an infinite loop to run our game
	clock.tick(60)						# Set the framerate to (typically 60fps)
	draw2
	player2.bottom += gravity			# Adding gravity in player2

	collide = pygame.Rect.colliderect(player1, player2) # Checke if player is colliding with platform or not using the colliderect() method. It will return a boolean value
	if collide:											# If the objects are colliding then changing the y coordinate
		player2.bottom = player1.top
		run=False

	
	pygame.draw.rect(window, (0, 255, 0),player1)		# Drawing player 1 rect
	pygame.draw.rect(window, (0, 0, 255),player2)		# Drawing player 2 rect
	pygame.display.update()								# Updating the display surface

pgzrun.go()