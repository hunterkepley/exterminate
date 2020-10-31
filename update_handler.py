import pygame
import game_handler

def update_game(g, dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
    
    game_handler.bug.Bug.update_bugs(g, dt)

    game_handler.sprayer.Sprayer.update_sprayers(g, dt)

    # FPS Printing
    #print(g.clock.get_fps())