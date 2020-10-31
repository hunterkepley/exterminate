import pygame
import update_handler as u
import render_handler as r
import person


class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 768))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUEGRAY = (100, 100, 150)

        self.person_list = []

    def init_game_objects(self):
        person.init_people(self)

    def run_game(self):
        dt = self.clock.tick(self.FPS) / 1000  # good ol' dt

        u.update_game(self, dt)
        r.render_game(self)