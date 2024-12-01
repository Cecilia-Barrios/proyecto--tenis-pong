import pygame

def cargar_sonido(ruta):
    return pygame.mixer.Sound(ruta)

def mostrar_texto(ventana, texto, tamano, x, y, color):
    fuente = pygame.font.Font(None, tamano)
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=(x, y))
    ventana.blit(superficie, rect)
