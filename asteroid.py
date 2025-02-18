import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

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
    
    # Split asteroids
    def split(self):
        # Always kill orginal asteroid
        self.kill()
        # Check for size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Create random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)
        # Set rotation vectors for each asteroid
        rot1 = self.velocity.rotate(angle)
        rot2 = self.velocity.rotate(-angle)
        # Reduce asteroid size
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create 2 new asteroids
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        # Set and speed up velocities
        ast1.velocity = rot1 * 1.2
        ast2.velocity = rot2 * 1.2


    

        