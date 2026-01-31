# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
# 
import pygame as pg
from pygame.rect import Rect

# https://pygame-gui.readthedocs.io/en/latest/index.html
#from pygame_gui.elements.ui_text_entry_line import UITextEntryLine

#import pgzrun

dblue = (0,0,128)
lblue=(0, 128, 255)

def main():
    print('main')
   #screen = pg.display.set_mode((640, 480))
    screen = pg.display.set_mode((300, 200))
    #screen.fill((255, 255, 255)) 						# Filling the window with white color
	#
    #font = pg.font.Font(None, 32)
    font = pg.font.SysFont(None, 14)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color(lblue)
    color_active = pg.Color(dblue)
    color = color_inactive
    active = False
    text = ''
    done = False
    print('debug 1')

    # gui_input_text = UITextEntryLine(relative_rect=Rect(0, 0, 100, 100), manager=manager)


    screen.fill((255, 30, 30))
    txt_surface = font.render(text, True, color)
    width = max(120, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pg.draw.rect(screen, color, input_box, 2)
    pg.display.update()								# Updating the display surface
    pg.display.flip()
    clock.tick(30)


def getUserInput():
    global utext
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
        if active:
            color = color_active
        else:
            color = color_passive
        txSurface = ufont.render(utext, True, txColour)  # text surface
          

#if __name__ == '__main__':
pg.init()
main()
pg.quit()

	
#pgzrun.go()