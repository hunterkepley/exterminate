import pygame
import game_handler
import sprayer

def update_game(g, dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if g.placing:
                game_handler.sticky_pad.StickyPad.spawn_sticky_pad(g, g.placer.position)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    
    if g.placing:
        g.placer.update(g, dt)

    game_handler.bug.Bug.update_bugs(g, dt)

    game_handler.sprayer.Sprayer.update_sprayers(g, dt)

    game_handler.sticky_pad.StickyPad.update_sticky_pads(g, dt)

    game_handler.bug.Bug.bug_spawn_handler(g)

    # FPS Printing
    #print(g.clock.get_fps())