import pygame
import random
import math

bug_images = ["./Assets/fly.png", "./Assets/ladybug.png", "./Assets/snail.png"]

class Bug():
    def __init__(self, position, velocity_dir):
        self.image = pygame.image.load(bug_images[random.randint(0, len(bug_images)-1)])
        self.rect = self.image.get_rect()
        self.speed = 10
        self.velocity_dir = velocity_dir
        self.velocity = [self.speed*velocity_dir[0], self.speed*velocity_dir[1]]
        self.rect.move_ip(*position)
        self.position = position

        self.checkpoint = 0 # movement checkout
        self.checkpoints = [
            pygame.Rect(184, 247, 40, 40), # 0
            pygame.Rect(378, 256, 40, 40), # 1
            pygame.Rect(464, 508, 40, 40), # 2
            pygame.Rect(406, 701, 40, 40), # 3
            pygame.Rect(753, 622, 40, 40), # 4
            pygame.Rect(741, 286, 40, 40), # 5
            pygame.Rect(553, 337, 40, 40), # 6
            pygame.Rect(567, 516, 40, 40), # 7
            pygame.Rect(882, 462, 40, 40), # 8
            pygame.Rect(1006, 78, 40, 20), # 9
            pygame.Rect(335, 71, 70, 100), # Pumpkin!
            pygame.Rect(0, 0, 0, 0)
        ]

        self.direction = 0 # 0 = left, 1 = up, 2 = right, 3 = down

        # Slow down from glue
        self.slowed_down = False
        self.speed_change = self.speed/2
        self.slow_down_timer = 30
        self.slow_down_timer_max = self.slow_down_timer

    def update(self, dt):

        # Decide direction
        if self.velocity[0] > 0:
            self.direction = 2
        elif self.velocity[1] < 0:
            self.direction = 0

        if self.velocity[1] > 0:
            self.direction = 1
        elif self.velocity[1] < 0:
            self.direction = 3

        if self.checkpoint == len(self.checkpoints)-1: # if at pumpkin
            print("end")
        else:
            self.follow_path()
            self.velocity = [self.speed*self.velocity_dir[0], self.speed*self.velocity_dir[1]]

            # Out of bounds check
            if self.position[0] > 1080 or self.position[0] < 0 or self.position[1] > 768 or self.position[1] < 0:
                self.rect.move_ip(self.velocity[0], self.velocity[1])
            else:
                self.rect.move_ip(self.velocity[0], self.velocity[1])

            
            self.position = [self.rect.left, self.rect.top]

            if self.slowed_down:
                self.slow_down()

    def follow_path(self):
        if self.checkpoints[self.checkpoint].colliderect(self.rect):
            self.checkpoint += 1

            # Calculate movement using an imaginary vector :)
            dx = self.checkpoints[self.checkpoint].left-self.checkpoints[self.checkpoint-1].left
            dy = self.checkpoints[self.checkpoint].top-self.checkpoints[self.checkpoint-1].top

            ln = math.sqrt(dx*dx+dy*dy)

            dx /= ln
            dy /= ln

            self.velocity_dir = [dx, dy]


    def slow_down(self):
        self.slow_down_timer -= 1
        if self.slow_down_timer <= 0:
            self.slow_down_timer = self.slow_down_timer_max
            self.slowed_down = False
            self.speed += self.speed_change


    # Static methods

    @staticmethod
    def bug_spawn_handler(g):
        g.bug_spawn_timer -= 1
        if g.bug_spawn_timer < 0:
            Bug.spawn_bug(g, [-5, 366], [1, -0.5])
            g.bug_spawn_timer_max -= 1
            g.bug_spawn_timer = g.bug_spawn_timer_max

    @staticmethod
    def spawn_bug(g, position, velocity_dir):
        g.bug_list.append(Bug(position, velocity_dir))

    @staticmethod
    def update_bugs(g, dt):
        for i in g.bug_list:
            i.update(dt)

    @staticmethod
    def render_bugs(g):
        for i in g.bug_list:

            rotated_image = pygame.transform.rotate(i.image, (i.direction * 90))

            g.screen.blit(rotated_image, i.rect)