import pygame
from constants import *
from player import *

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
    
    # Create containers
    Player.containers = (updatable, drawable)

    # Create plyer
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update based on the keyboard
        updatable.update(dt)

        # Draw the game
        # Clear the screen
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Calculate delta time
        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()