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
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        # Clear the screen
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update the player based on the keyboard
        player_one.update(dt)

        # Draw the player
        player_one.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Calculate delta time
        dt = game_clock.tick() / 1000
        

if __name__ == "__main__":
    main()