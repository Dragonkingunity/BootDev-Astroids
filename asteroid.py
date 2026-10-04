import pygame
import random

from ast import AST

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position +=  self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            a_velocity = self.velocity.rotate((random_angle))
            b_velocity = self.velocity.rotate((-random_angle))

            n_radius = self.radius - ASTEROID_MIN_RADIUS

            Asteroid(self.position.x, self.position.y, n_radius).velocity = a_velocity * 1.2
            Asteroid(self.position.x, self.position.y, n_radius).velocity = b_velocity * 1.2
