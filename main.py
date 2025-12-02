import pygame
import utilidades.constantes as datos
import funciones.funcion_principal as funcion
import funciones.pantalla_inicio
import utilidades.imagenes as imagen
#soundimage.com
pygame.init()
pygame.display.set_caption(datos.TITULO)
pygame.display.set_icon(imagen.icono)

funciones.pantalla_inicio.pantalla_inicio()

funcion.principal()