import pygame
import random

bug_images = ["./Assets/fly.png", "./Assets/ladybug.png", "./Assets/snail.png"]

class Bug():
    def __init__(self, position):
        self.image = pygame.image.load(bug_images[random.randint(0, len(bug_images)-1)])
        self.rect = self.image.get_rect()
        self.velocity = [0, 0]
        self.speed = 100
        self.rect.move_ip(*position)
        self.position = position

        self.moveTimer = 0
        self.moveTimerMax = random.randrange(10, 70)

        self.direction = 0 # 0 = left, 1 = up, 2 = right, 3 = down

    def update(self, dt):
        if self.moveTimer <= 0:

            # Random speed decision
            self.velocity[0] = random.randrange(self.speed) * dt
            self.velocity[1] = random.randrange(self.speed) * dt
            if self.velocity[0] > 0:
                self.direction = 2
            if self.velocity[1] > 0:
                self.direction = 1
            # Left/right and up/down
            x_reverse = random.randrange(2)*-1
            y_reverse = random.randrange(2)*-1
            if x_reverse != 0:
                self.velocity[0] *= x_reverse
                self.direction = 0
            if y_reverse != 0:
                self.velocity[1] *= y_reverse
                self.direction = 3


            self.moveTimer = self.moveTimerMax
        else:
            self.moveTimer -= 1

        # Out of bounds check
        if self.position[0] > 1080 or self.position[0] < 0 or self.position[1] > 768 or self.position[1] < 0:
            self.rect.move_ip([self.velocity[0]*-1, self.velocity[1]*-1])
        else:
            self.rect.move_ip(*self.velocity)
        
        self.position = [self.rect.left, self.rect.top]

    # Static methods

    @staticmethod
    def init_bugs(g):
        for i in range(0, 30):
            g.bug_list.append(Bug([random.randrange(1080), random.randrange(768)]))

    @staticmethod
    def spawn_bug(g):
        g.bug_list.append(Bug([random.randrange(1080), random.randrange(768)]))

    @staticmethod
    def update_bugs(g, dt):
        for i in g.bug_list:
            i.update(dt)

    @staticmethod
    def render_bugs(g):
        for i in g.bug_list:

            rotated_image = pygame.transform.rotate(i.image, (i.direction * 90))

            g.screen.blit(rotated_image, i.rect)