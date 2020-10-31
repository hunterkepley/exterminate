import pygame
import game_handler
import sprayer

def update_game(g, dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if g.placing:
                sprayer.Sprayer.spawn_sprayer(g, g.placer.position)
    
    if g.placing:
        g.placer.update(g, dt)

    game_handler.bug.Bug.update_bugs(g, dt)

    game_handler.sprayer.Sprayer.update_sprayers(g, dt)

    # FPS Printing
    #print(g.clock.get_fps())