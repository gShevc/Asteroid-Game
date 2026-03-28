import pygame
import random
from logger import log_event
from constants import  *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position) , self.radius,LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vector_a = self.velocity.rotate(angle)
            vector_b = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #Create 2 new asteroids at this location
            newAsteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            newAsteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            newAsteroid1.velocity = vector_a * 1.2
            newAsteroid2.velocity = vector_b



