import pygame
import game_handler

def render_game(g):
    g.screen.fill(g.BLUEGRAY)

    game_handler.person.Person.render_people(g)
    