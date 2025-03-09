# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



#unused clock object
class Clock:
    def __init__(self, fps: int = 60):
        self._fps = fps
        self._clock: pygame.time.Clock = pygame.time.Clock()

    @property
    def fps(self):
        return self._fps
    
    def set_framerate(self, fps: int):
        self._fps = fps

    def tick(self):
        self._clock.tick(self._fps)
        

def main():
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock() 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
