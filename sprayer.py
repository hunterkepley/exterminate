import pygame

class Sprayer():
    def __init__(self, position):
        self.base_image = pygame.image.load("./Assets/towerbase.png")
        self.top_image = pygame.image.load("./Assets/sprayer.png")
        self.base_rect = self.base_image.get_rect()
        self.top_rect = self.top_image.get_rect()
        self.base_rect.move_ip(*position)
        self.top_rect.move_ip(*position)
        self.v = 0

    def update(self, dt):
        print('',end='')


    # Static methods

    @staticmethod
    def spawn_sprayer(g, position):
        g.sprayer_list.append(Sprayer(position))

    @staticmethod
    def update_sprayers(g, dt):
        for i in g.sprayer_list:
            i.update(dt)

    @staticmethod
    def render_sprayers(g):
        for i in g.sprayer_list:
            g.screen.blit(i.base_image, i.base_rect)

            i.v+=1

            center = i.top_rect.center
            rotated_top_image = pygame.transform.rotate(i.top_image, i.v)
            new_rect = rotated_top_image.get_rect(center = center)

            g.screen.blit(rotated_top_image, new_rect)