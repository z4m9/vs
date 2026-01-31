# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
# 
import pygame as pg
import pgzrun

dblue = (0,0,128)
lblue=(0, 128, 255)
dgreen = (0,255,128)
lgreen=(0, 255, 255)
lred=(255, 30, 30)
brown=(100, 30, 30)

def main():
    print('main')
   #screen = pg.display.set_mode((640, 480))
    
    screen.fill(dgreen) 						# Filling the window with color
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

    while not done:
       # print('looping')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('quit ',active)
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                print('mouse ',active)
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                print('key ',active)
            #if active:
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode


    screen.fill(lred)
    txt_surface = font.render(text, True, color)
    width = max(120, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pg.draw.rect(screen, color, input_box, 2)
    pg.display.update()								# Updating the display surface
    pg.display.flip()
    clock.tick(30)

#if __name__ == '__main__':
pg.init()
# screen is display surface object of specific dimension
screen = pg.display.set_mode((300, 200))
screen.fill(lgreen)
main()
# pg.quit()

	
pgzrun.go()