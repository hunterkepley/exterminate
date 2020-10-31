import pygame
import game_handler

def render_game(g):
    g.screen.fill(g.BROWN)
    g.screen.blit(g.bg, g.bg.get_rect())


    game_handler.bug.Bug.render_bugs(g)
    game_handler.sprayer.Sprayer.render_sprayers(g)

    if g.placing:
        g.placer.render(g)
    