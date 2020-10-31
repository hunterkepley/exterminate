import pygame
import game_handler

def render_game(g):
    g.screen.fill(g.BROWN)
    g.screen.blit(g.bg, g.bg.get_rect())

    game_handler.bug.Bug.render_bugs(g)
    