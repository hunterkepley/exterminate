import pygame
import random

class Bug(pygame.sprite.Sprite):
    def __init__(self, position, color):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
        self.speed = 100
        self.rect.move_ip(*position)

        self.moveTimer = 0
        self.moveTimerMax = random.randrange(20, 70)

    def update(self, dt):
        if self.moveTimer <= 0:
            # Random speed decision`
            self.velocity[0] = random.randrange(self.speed) * dt
            self.velocity[1] = random.randrange(self.speed) * dt
            # Left/right and up/down
            x_reverse = random.randrange(2)*-1
            y_reverse = random.randrange(2)*-1
            if x_reverse != 0:
                self.velocity[0] *= x_reverse
            if y_reverse != 0:
                self.velocity[1] *= y_reverse


            self.moveTimer = self.moveTimerMax
        else:
            self.moveTimer -= 1

        self.rect.move_ip(*self.velocity)

    # Static methods

    @staticmethod
    def init_bugs(g):
        for i in range(0, 30):
            g.bug_list.append(Bug([random.randrange(1080), random.randrange(768)], g.WHITE))

    @staticmethod
    def spawn_bug(g):
        g.bug_list.append(Bug([random.randrange(1080), random.randrange(768)], g.WHITE))

    @staticmethod
    def update_bugs(g, dt):
        for i in g.bug_list:
            i.update(dt)

    @staticmethod
    def render_bugs(g):
        for i in g.bug_list:
            g.screen.blit(i.image, i.rect)