import pygame
import math
import random

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
        self.spray_timer = 10
        self.spray_timer_max = self.spray_timer

    def update(self, g, dt):
        self.spray(g)

    def spray(self, g):
        self.spray_timer -= 1
        if self.spray_timer <= 0:
            self.poison_clouds.append(PoisonCloud(self.rotation, [self.base_rect.left, self.base_rect.top]))
            self.spray_timer = self.spray_timer_max

    # Static methods

    @staticmethod
    def spawn_sprayer(g, position):
        g.sprayer_list.append(Sprayer(position))

    @staticmethod
    def update_sprayers(g, dt):
        for i in g.sprayer_list:
            i.update(g, dt)
            for j in i.poison_clouds:
                j.update(g, dt)
                if j.remove:
                    i.poison_clouds.remove(j)
                    

    @staticmethod
    def render_sprayers(g):
        for i in g.sprayer_list:
            g.screen.blit(i.base_image, i.base_rect)

            i.rotation+=5

            center = i.top_rect.center
            rotated_top_image = pygame.transform.rotate(i.top_image, i.rotation)
            new_rect = rotated_top_image.get_rect(center = center)

            g.screen.blit(rotated_top_image, new_rect)

            for j in i.poison_clouds:
                center = i.top_rect.center
                rotated_image = pygame.transform.rotate(j.image, j.rotation)
                g.screen.blit(rotated_image, j.rect)

class PoisonCloud():
    def __init__(self, angle, position):
        self.image = pygame.image.load("./Assets/poison.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(position)
        self.move_speed = 200
        self.angle = angle
        self.moved = 0
        self.range = 30
        self.remove = False
        self.rotation = random.randint(0, 360)
        self.health = 3

    def update(self, g, dt):
        a = self.angle-100
        self.rect.move_ip([self.move_speed * dt * math.sin((math.pi/180)*a), self.move_speed * dt * math.cos((math.pi/180)*a)])
        self.moved += 1

        if self.moved > self.range:
            self.remove = True
        
        for b in g.bug_list:
            if b.rect.colliderect(self.rect) and self.health >= 0:
                b.health -= 1
                self.health -= 1
        
        if self.health <= 0:
            self.remove = True
