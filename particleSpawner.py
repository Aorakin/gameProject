from tkinter import Y
import pygame
from particle import Particle
import random  

class ParticleSpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.particle_group = pygame.sprite.Group()

    def update(self):
        self.particle_group.update()
        for enemy in  self.enemy_group:
            if enemy.rect.y<=0:
                self.enemy_group.remove(enemy)
    def spawn_particles(self,pos):
        random_number = random.randrange(3,30)
        for number_particles in range(random_number):
            number_particles = Particle()
            number_particles.rect.x = pos[0]
            number_particles.rect.y = pos[1]
            self.particle_group.add(number_particles)
