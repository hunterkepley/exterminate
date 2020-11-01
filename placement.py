import pygame

class Placer():
    def __init__(self):
        self.image = pygame.image.load("./Assets/selector.png")
        self.rect = self.image.get_rect()
        self.position = [0, 0] # Position of object to be placed

        self.object = 0 # 0 = sprayer, 1 = sticky pad, 2 = bear trap
        self.objects = [
            'sprayer',
            'sticky_pad',
        ]

    def update(self, g, dt):
        self.rect.left = pygame.mouse.get_pos()[0]-20
        self.rect.top = pygame.mouse.get_pos()[1]-20
        self.position = [self.rect.left, self.rect.top]

    def render(self, g):
        g.screen.blit(self.image, self.rect)