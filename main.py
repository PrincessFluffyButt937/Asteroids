# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shoot import *



def main():
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids = pygame.sprite.Group()
    Shots = pygame.sprite.Group()
    Asteroid.containers = (Asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (Shots, updatable, drawable)
    Asteroid_f = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for ast in Asteroids:
            if player.collision(ast):
                print("Game over!")
                sys.exit()
            for bullet in Shots:
                if bullet.collision(ast): 
                    bullet.kill()
                    ast.split()
        updatable.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()
