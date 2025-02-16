import pygame
from circleshape import *

class Asteroid(CircleShape):

    # Initialization method
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # Override draw() method
    def draw(self, screen):
        # Asteroids are drawn as circles
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    # Override update() method
    def update(self, dt):
        self.position += self.velocity * dt