import pygame

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
        self.sprayTimer = 5
        self.sprayTimerMax = self.sprayTimer

    def update(self, g, dt):
        self.spray(g)

    def spray(self, g):
        self.poison_clouds.append(PoisonCloud(self.base_rect.center))

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
    def __init__(self, position):
        self.image = pygame.image.load("./Assets/selector.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(position)
        self.move_speed = 1

    def update(self, dt):
        self.rect.move_ip([self.move_speed, self.move_speed])