import pygame
from modulos.clases import Pelota, Paleta
from modulos.configuraciones import *
from modulos.logica import reiniciar_pelota
from modulos.funciones_auxiliares import mostrar_texto

pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption(" PONG ")
reloj = pygame.time.Clock()

# Elementos del juego
pelota = Pelota(ANCHO_VENTANA // 2, ALTO_VENTANA // 2, TAMANO_PELOTA, VELOCIDAD_INICIAL_PELOTA)
paleta_izquierda = Paleta(20, ALTO_VENTANA // 2 - ALTO_PALETA // 2, ANCHO_PALETA, ALTO_PALETA)
paleta_derecha = Paleta(ANCHO_VENTANA - 40, ALTO_VENTANA // 2 - ALTO_PALETA // 2, ANCHO_PALETA, ALTO_PALETA)

# Variables de puntuación
puntaje_izquierdo = 0
puntaje_derecho = 0

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        paleta_izquierda.velocidad = -VELOCIDAD_PALETA
    elif teclas[pygame.K_s]:
        paleta_izquierda.velocidad = VELOCIDAD_PALETA
    else:
        paleta_izquierda.velocidad = 0

    if teclas[pygame.K_UP]:
        paleta_derecha.velocidad = -VELOCIDAD_PALETA
    elif teclas[pygame.K_DOWN]:
        paleta_derecha.velocidad = VELOCIDAD_PALETA
    else:
        paleta_derecha.velocidad = 0

    # Movimiento
    paleta_izquierda.mover()
    paleta_derecha.mover()
    pelota.mover()

    # Detección de colisiones
    if pelota.rect.colliderect(paleta_izquierda.rect) or pelota.rect.colliderect(paleta_derecha.rect):
        pelota.rebotar("horizontal")

    if pelota.rect.top <= 0 or pelota.rect.bottom >= ALTO_VENTANA:
        pelota.rebotar("vertical")

    if pelota.rect.left <= 0:
        puntaje_derecho += 1
        reiniciar_pelota(pelota)
    elif pelota.rect.right >= ANCHO_VENTANA:
        puntaje_izquierdo += 1
        reiniciar_pelota(pelota)

    # Dibujar elementos
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, BLANCO, pelota.rect)
    pygame.draw.rect(ventana, BLANCO, paleta_izquierda.rect)
    pygame.draw.rect(ventana, BLANCO, paleta_derecha.rect)

    # Mostrar puntuación
    mostrar_texto(ventana, f"{puntaje_izquierdo} - {puntaje_derecho}", 36, ANCHO_VENTANA // 2, 30, BLANCO)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

