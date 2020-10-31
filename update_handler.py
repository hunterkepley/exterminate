import pygame
import game_handler

def update_game(g, dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
    
    game_handler.person.Person.update_people(g, dt)

    # FPS Printing
    #print(g.clock.get_fps())