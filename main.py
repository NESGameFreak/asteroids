import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        screen.fill((0, 0, 0))
        player_one.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
       
        dt = game_clock.tick() / 1000
        pygame.display.flip()
    #print("Starting asteroids!")
    #print("Screen width: 1280")
    #print("Screen height: 720")

if __name__ == "__main__":
    main()