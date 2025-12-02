import pygame
import utilidades.constantes as datos
import funciones.funcion_principal as funcion
import funciones.pantalla_inicio
#soundimage.com
pygame.init()

pygame.display.set_caption(datos.TITULO)

funciones.pantalla_inicio.pantalla_inicio()

funcion.principal()