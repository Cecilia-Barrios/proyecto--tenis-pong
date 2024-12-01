import pygame
from modulos.configuraciones import BLANCO, ANCHO_VENTANA, ALTO_VENTANA

class Pelota:
    def __init__(self, x, y, tamano, velocidad):
        self.rect = pygame.Rect(x, y, tamano, tamano)
        self.velocidad_x = velocidad
        self.velocidad_y = velocidad

    def mover(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

    def rebotar(self, direccion):
        if direccion == "vertical":
            self.velocidad_y *= -1
        elif direccion == "horizontal":
            self.velocidad_x *= -1

class Paleta:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.velocidad = 0

    def mover(self):
        self.rect.y += self.velocidad
        self.rect.y = max(0, min(self.rect.y, ALTO_VENTANA - self.rect.height))
