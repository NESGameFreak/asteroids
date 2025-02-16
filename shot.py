import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        # Initializaing inheritance
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        # Asteroids are drawn as circles
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt