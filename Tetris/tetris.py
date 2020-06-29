import pygame
from init import *

filled = []
pause  = False



pygame.init()
pygame.display.set_caption('tetRIS')
win = pygame.display.set_mode(sc_size)
win.fill(color_bg)

colors = [(225, 125, 0), (0, 225, 125), (0, 125, 225)]  
index_color = 0  

pos_x = cnt_w // 2
pos_y = 1
pygame.draw.rect(win, colors[index_color], (pos_x*r, pos_y*r, r, r), 3)
pygame.display.update()

clock = pygame.time.Clock()
fall_time = 0
interval = 300  
press_time = 0
int_pressed = 100  




while True:
    clock.tick()
    fall_time += clock.get_rawtime()
    press_time += clock.get_rawtime()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
            pause = not pause
    if  pause == False:   
        if press_time >= int_pressed:
            press_time = 0
            key = pygame.key.get_pressed() 
            if pos_y < cnt_h - 1:  
                if pos_x > 0 and key[pygame.K_LEFT]:
                    pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                    pos_x -= 1
                if pos_x < cnt_w - 1 and key[pygame.K_RIGHT]:
                    pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                    pos_x += 1
                if pos_x < cnt_w - 1 and key[pygame.K_DOWN]:
                    if (cnt_h - 1, pos_x) not in filled:
                        pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                        pos_y = cnt_h - 1
                    else:
                        pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                        while (pos_y, pos_x) not in filled:
                            pos_y += 1
                        pos_y -= 1

        if fall_time >= interval:
            fall_time = 0
            if pos_y < cnt_h - 1 and (pos_y+1,pos_x) not in filled:
                pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                pos_y += 1
            else:
                pygame.draw.rect(win, colors[index_color], (pos_x * r, pos_y * r, r, r)) 
                filled.append((pos_y,pos_x))
                pos_y = 1
                pos_x = cnt_w // 2
                index_color = (index_color + 1) % len(colors)

                
        if pos_y < cnt_h - 1:
            pygame.draw.rect(win, colors[index_color], (pos_x * r, pos_y * r, r, r), 3)  # контур квадрата
        else:
            pygame.draw.rect(win, colors[index_color], (pos_x * r, pos_y * r, r, r))  # заливка квадрата


    pygame.display.update()
    




