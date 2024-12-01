import random
from modulos.configuraciones import ANCHO_VENTANA, ALTO_VENTANA

def reiniciar_pelota(pelota):
    pelota.rect.x = ANCHO_VENTANA // 2 - pelota.rect.width // 2
    pelota.rect.y = ALTO_VENTANA // 2 - pelota.rect.height // 2
    pelota.velocidad_x *= random.choice([-1, 1])
    pelota.velocidad_y *= random.choice([-1, 1])

