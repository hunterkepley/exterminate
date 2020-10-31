import pygame
import person
import game_handler as game

"""

UNCC Fall 2020 Game Jam

Game developed by Hunter Kepley

"""


def main():

    pygame.init()

    pygame.display.set_caption("e x t e r m i n a t e")

    g = game.Game()

    person.Person.init_people(g)

    while g.running:
        
        g.run_game()

        pygame.display.update()

    quit()

if __name__ == "__main__":
    main()