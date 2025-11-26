import pygame
import utilidades.constantes as datos
from utilidades.juego import juego
from utilidades.pantalla_final import pantalla_final
pygame.mixer.init()

sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

def jugar():
    sonido_boton.set_volume(datos.volumen)
    sonido_boton.play()
    puntaje = 0
    dificultad = ""
    match datos.dificultad:
        case "facil":
            puntaje, dificultad = juego(ventana_juego = ventana, velocidad_pelota = 5, tiempo = 20000, probabilidad_juego = 8, fila_bloques = 6, columna_bloques = 10, dificultad=datos.dificultad)
        case "medio":
            puntaje, dificultad = juego(ventana_juego = ventana, velocidad_pelota = 5.5, tiempo = 13000, probabilidad_juego = 10, fila_bloques = 7, columna_bloques = 10, dificultad=datos.dificultad)
        case "dificil":
            puntaje, dificultad = juego(ventana_juego = ventana, velocidad_pelota = 6, tiempo = 8000, probabilidad_juego = 15, fila_bloques = 9, columna_bloques = 10, dificultad=datos.dificultad)
        case "imposible":
            juego(ventana_juego = ventana, velocidad_pelota = 5.2, tiempo = 8000, probabilidad_juego = 15, fila_bloques = 10, columna_bloques = 10, dificultad=datos.dificultad)
    pantalla_final(ventana=ventana, puntaje=puntaje, dificultad=dificultad)