import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid, Shot
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)
        dt = dt / 1000

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            collision_detected = player.check_collision(asteroid)
            if collision_detected:
                print("Game over!")
                sys.exit()
       
            for bullet in bullets:
                collision_detected = bullet.check_collision(asteroid)
                if collision_detected:
                    asteroid.split()
                    bullet.kill()

        for draw in drawable:
            draw.draw(screen)    

        pygame.display.flip()

if __name__ == "__main__":
    main()
