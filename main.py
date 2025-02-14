import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    #print("Starting asteroids!")
    #print("Screen width: 1280")
    #print("Screen height: 720")

if __name__ == "__main__":
    main()