import pygame
import update_handler as u
import render_handler as r
import menu_handler as m
import bug
import sprayer
import placement
import sticky_pad
import money


class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1080, 768))
        self.screen_size = [1080, 768]
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUEGRAY = (0, 0, 10)
        self.BROWN = (150, 125, 100)

        self.bg = pygame.image.load("./Assets/bg.png")

        self.menu_image = pygame.image.load("./Assets/menu.png")
        self.menu_chooser = pygame.image.load("./Assets/menu_chooser.png")
        self.menu_state = 0 # 0 = play, 1 = quit

        self.bug_spawn_timer = 400
        self.bug_wave_amount = 1
        self.bug_spawn_offset = 5
        self.bug_spawn_offset_max = self.bug_spawn_offset
        self.bug_wave_amount_max = self.bug_wave_amount
        self.bug_spawn_timer_max = self.bug_spawn_timer

        self.bug_list = []
        self.sprayer_list = []
        self.sticky_pads = []

        self.placer = placement.Placer()
        self.placing = True
        self.object_image = pygame.image.load("./Assets/object_sprayer.png")

        self.store = money.Store()

        self.pumpkin_health = 10

        # Font
        pygame.font.init()
        self.game_font = pygame.font.SysFont('Comic Sans MS', 30) # i promise it doesnt look like it

        self.in_game = False

    def init_game_objects(self):
        print("Should init the food")

    def run_game(self):
        dt = self.clock.tick(self.FPS) / 1000  # good ol' dt

        if self.in_game:
            u.update_game(self, dt)
            r.render_game(self)
        else: # in menu
            m.update_menu(self)
            m.render_menu(self)