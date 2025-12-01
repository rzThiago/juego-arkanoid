import pygame
import utilidades.constantes as datos
ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

def hover():
    boton= datos.botones[5]
    mouse_pos = pygame.mouse.get_pos()
    if pygame.Rect(300, 460, 220, 45).collidepoint(mouse_pos):
        print("Estoy en el boton")
        if not boton["hover"]:
            boton["hover"] = True
        color = (0, 0, 255)
    else:
        print("NO estoy en el boton")
        boton["hover"] = False
        color = (0, 0, 0)

    pygame.draw.rect(ventana, color, pygame.Rect(300, 460, 220, 45),4)
