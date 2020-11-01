import pygame
import math

class Sprayer():
    def __init__(self, position):
        self.base_image = pygame.image.load("./Assets/towerbase.png")
        self.top_image = pygame.image.load("./Assets/sprayer.png")

        self.base_rect = self.base_image.get_rect()
        self.top_rect = self.top_image.get_rect()

        self.base_rect.move_ip(*position)
        self.top_rect.move_ip(*position)

        self.rotation = 0

        self.poison_clouds = []
        self.sprayTimer = 10
        self.sprayTimerMax = self.sprayTimer

    def update(self, g, dt):
        self.spray(g)

    def spray(self, g):
        self.sprayTimer -= 1
        if self.sprayTimer <= 0:
            self.poison_clouds.append(PoisonCloud(self.rotation, [self.base_rect.left, self.base_rect.top]))
            self.sprayTimer = self.sprayTimerMax

    # Static methods

    @staticmethod
    def spawn_sprayer(g, position):
        g.sprayer_list.append(Sprayer(position))

    @staticmethod
    def update_sprayers(g, dt):
        for i in g.sprayer_list:
            i.update(g, dt)
            for j in i.poison_clouds:
                j.update(dt)
                if j.remove:
                    i.poison_clouds.remove(j)
                    

    @staticmethod
    def render_sprayers(g):
        for i in g.sprayer_list:
            g.screen.blit(i.base_image, i.base_rect)

            i.rotation+=1

            center = i.top_rect.center
            rotated_top_image = pygame.transform.rotate(i.top_image, i.rotation)
            new_rect = rotated_top_image.get_rect(center = center)

            g.screen.blit(rotated_top_image, new_rect)

            for j in i.poison_clouds:
                g.screen.blit(j.image, j.rect)

class PoisonCloud():
    def __init__(self, angle, position):
        self.image = pygame.image.load("./Assets/selector.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(position)
        self.move_speed = 150
        self.angle = angle
        self.moved = 0
        self.range = 30
        self.remove = False

    def update(self, dt):
        self.rect.move_ip([(self.move_speed * math.sin(self.angle)) * dt, (self.move_speed * math.cos(self.angle)) * dt])
        self.moved += 1
        if self.moved > self.range:
            self.remove = True
