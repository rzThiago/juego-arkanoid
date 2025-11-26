import pygame
import utilidades.constantes as datos

pygame.mixer.init()

sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
def continuar():
    sonido_boton.set_volume(datos.volumen)
    sonido_boton.play()
    print("Continuar...")