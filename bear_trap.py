import pygame


class BearTrap():
    def __init__(self, position):
        self.image = pygame.image.load("./Assets/beartrapopen.png")

        self.rect = self.image.get_rect()

        self.rect.move_ip(*position)

        self.active = True

    def update(self, g, dt):
        if self.active:
            for b in g.bug_list:
                if b.rect.colliderect(self.rect):
                    self.image = pygame.image.load("./Assets/beartrapclosed.png")
                    b.health -= 2
                    self.active = False


    # Static methods

    @staticmethod
    def spawn_bear_trap(g, position):
        g.bear_traps.append(BearTrap(position))

    @staticmethod
    def update_bear_traps(g, dt):
        for i in g.bear_traps:
            i.update(g, dt)

    @staticmethod
    def render_bear_traps(g):
        for i in g.bear_traps:
            g.screen.blit(i.image, i.rect)