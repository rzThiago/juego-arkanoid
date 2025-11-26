import pygame
import utilidades.constantes as datos

pygame.mixer.init()
sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")

def creditos():
    sonido_boton.set_volume(datos.volumen)
    sonido_boton.play()
    print("Creditos...")
    print(f"Dificultad = {datos.dificultad} Volumen = {datos.volumen}")