import pygame

class Person(pygame.sprite.Sprite):
    def __init__(self, position, color):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
        self.speed = 100
        self.rect.move_ip(*position)

    def update(self, dt):
        self.velocity[0] = self.speed * dt
        self.rect.move_ip(*self.velocity)

    @staticmethod
    def init_people(g):
        for i in range(0, 30):
            g.person_list.append(Person([0, 26*i], g.WHITE))

    @staticmethod
    def update_people(g, dt):
        for i in g.person_list:
            i.update(dt)

    @staticmethod
    def render_people(g):
        for i in g.person_list:
            g.screen.blit(i.image, i.rect)