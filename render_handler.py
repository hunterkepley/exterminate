import pygame
import game_handler

def render_game(g):
    g.screen.fill(g.BROWN)
    g.screen.blit(g.bg, g.bg.get_rect())


    game_handler.sticky_pad.StickyPad.render_sticky_pads(g)
    game_handler.bug.Bug.render_bugs(g)
    game_handler.sprayer.Sprayer.render_sprayers(g)

    if g.placing:
        g.placer.render(g)

        object_rect = g.object_image.get_rect()
        object_rect.left = g.screen_size[0]/2-50
        g.screen.blit(g.object_image, object_rect)

    t = g.game_font.render("Money: {}".format(g.store.money), False, (0, 0, 0))
    g.screen.blit(t, (0,0))
    t = g.game_font.render("{}".format(g.pumpkin_health), False, (0, 0, 0))
    g.screen.blit(t, (345, 70))
    t = g.game_font.render("Score: {}".format(g.score), False, (255, 255, 255))
    g.screen.blit(t, (0, 20))
    