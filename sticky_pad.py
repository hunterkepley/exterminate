import pygame


class StickyPad():
    def __init__(self, position):
        self.image = pygame.image.load("./Assets/gluepad.png")

        self.rect = self.image.get_rect()

        self.rect.move_ip(*position)

    def update(self, g, dt):
        self.sticky(g)

    def sticky(self, g):
        for b in g.bug_list:
            if b.rect.colliderect(self.rect) and not b.slowed_down:
                b.slowed_down = True
                b.speed -= b.speed_change

    # Static methods

    @staticmethod
    def spawn_sticky_pad(g, position):
        g.sticky_pads.append(StickyPad(position))

    @staticmethod
    def update_sticky_pads(g, dt):
        for i in g.sticky_pads:
            i.update(g, dt)

    @staticmethod
    def render_sticky_pads(g):
        for i in g.sticky_pads:
            g.screen.blit(i.image, i.rect)