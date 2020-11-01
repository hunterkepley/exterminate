import pygame
import update_handler as u
import render_handler as r
import bug
import sprayer
import placement
import sticky_pad


class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 768))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUEGRAY = (0, 0, 10)
        self.BROWN = (150, 125, 100)

        self.bg = pygame.image.load("./Assets/bg.png")

        self.bug_spawn_timer = 200
        self.bug_spawn_timer_max = self.bug_spawn_timer

        self.bug_list = []
        self.sprayer_list = []
        self.sticky_pads = []

        self.placer = placement.Placer()
        self.placing = True

    def init_game_objects(self):
        print("Should init the food")

    def run_game(self):
        dt = self.clock.tick(self.FPS) / 1000  # good ol' dt

        u.update_game(self, dt)
        r.render_game(self)