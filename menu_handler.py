import pygame

def update_menu(g):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if g.menu_state == 0:
                    g.in_game = True
                else:
                    g.running = False
            if event.key == pygame.K_DOWN:
                if g.menu_state == 0:
                    g.menu_state = 1
                else:
                    g.menu_state = 0
            elif event.key == pygame.K_UP:
                if g.menu_state == 1:
                    g.menu_state = 0
                else:
                    g.menu_state = 1

def render_menu(g):
    g.screen.blit(g.menu_image, g.menu_image.get_rect())
    rect = g.menu_chooser.get_rect()
    if g.menu_state == 0:
        rect.top = g.screen_size[1]/2+90
        rect.left = g.screen_size[0]/2-117
    else:
        rect.top = g.screen_size[1]-155
        rect.left = g.screen_size[0]/2-117

    g.screen.blit(g.menu_chooser, rect)