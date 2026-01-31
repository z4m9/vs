# https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/?ref=lbp
# import sys module
import pygame
import sys

pygame.init()                                   # initialize all imported module
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])    # it will display on screen
ufont = pygame.font.Font(None, 32)              # basic font for user typing
utext = ''                                      # users input text
inRect = pygame.Rect(200, 200, 140, 32)         # input rectangle
color_active = pygame.Color('darkblue')         # color_active stores color(lightskyblue3) which gets active when input box is clicked by user
color_passive = pygame.Color('darkgreen')      # color_passive store color which is color of input box.
txColour = (20, 255, 255)                      # text colour
color = color_passive
active = False

def draw():
	global active, utext
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:                       # if user types QUIT then the screen will close
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if inRect.collidepoint(event.pos):
					active = True
				else:
					active = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:             # Check for backspace
					utext = utext[:-1]                          # get text input from 0 to -1 i.e. end.
				else:                                           # Unicode standard is used for string formation
					utext += event.unicode
		
		screen.fill((255, 255, 255))                            # set background color of screen
		if active:
			color = color_active
		else:
			color = color_passive
			
		pygame.draw.rect(screen, color, inRect)             # draw rectangle and argument passed which should be on screen
		txSurface = ufont.render(utext, True, txColour)  # text surface
		screen.blit(txSurface, (inRect.x+5, inRect.y+5)) # render at position stated in arguments
		inRect.w = max(100, txSurface.get_width()+10)    # set width of textfield so that text cannot get outside of user's text input
		pygame.display.flip()                           # display.flip() will update only a portion of the screen to updated, not full area
draw()
clock.tick(60)                                  # for every second at most 60 frames should be passed.
# end
