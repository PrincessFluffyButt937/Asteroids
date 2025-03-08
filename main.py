# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    while True:
        pygame.Surface.fill(screen, (0,0,0))

        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
