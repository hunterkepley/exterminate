import pygame

class Swatter():
    def __init__(self):
        self.image = pygame.image.load("./Assets/swatter.png")
        self.rect = image.get_rect()

    def update(self):
        print("test")


    # Static methods
    
    @staticmethod
    def update_swatters(g, dt):
        for i in g.swatter_list:
            i.update(dt)

    @staticmethod
    def render_swatters(g):
        for i in g.swatter_list:

            g.screen.blit(i.image, i.rect)