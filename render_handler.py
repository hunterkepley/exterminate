import pygame
import game_handler

def render_game(g):
    g.screen.fill(g.BLUEGRAY)

    game_handler.bug.Bug.render_bugs(g)
    