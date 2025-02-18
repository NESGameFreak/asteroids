import pygame
import sys
from asteroid import *
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    # Initialize game
    pygame.init()

    #Setup display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)

    # Set clock
    game_clock = pygame.time.Clock()
    
    # Delta time initializer
    dt = 0

    # Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Create containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Create objects
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    falling_rocks = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update based on the keyboard
        updatable.update(dt)

        # Clear the screen
        screen.fill("black")
        
        # Draw the game
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()

        # Check for collisions
        for asteroid in asteroids:
            # Asteroids vs players
            if player_one.collision_detection(asteroid):
                print("Game Over!")
                sys.exit()

            # Shots vs asteroids
            for shot in shots:
                if asteroid.collision_detection(shot):
                    shot.kill()
                    asteroid.kill()
                
            
        # Calculate delta time for 60 fps
        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()