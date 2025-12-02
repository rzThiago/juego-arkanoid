import pygame
import utilidades.constantes as datos
ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

def funcion_hover(numero_boton):

    boton= datos.botones[numero_boton]
    print(boton["rect"])
    mouse_pos = pygame.mouse.get_pos()
    if boton["rect"].collidepoint(mouse_pos):
        print("Estoy en el boton")
        if not boton["hover"]:
            boton["hover"] = True
        color = (0, 0, 255)
    else:
        print("NO estoy en el boton")
        boton["hover"] = False
        color = (0, 0, 0)

    pygame.draw.rect(ventana, color, boton["rect"],4)
    if numero_boton == 8 or numero_boton == 9 or numero_boton == 10 or numero_boton == 12:
        if datos.dificultad=="facil":
            pygame.draw.rect(ventana, (0, 0, 255), datos.botones[8]["rect"],4)
        elif datos.dificultad=="medio":
            pygame.draw.rect(ventana, (0, 0, 255), datos.botones[9]["rect"],4)
        elif datos.dificultad=="dificil":
            pygame.draw.rect(ventana, (0, 0, 255), datos.botones[10]["rect"],4)
        else :
            pygame.draw.rect(ventana, (0, 0, 255), datos.botones[12]["rect"],4)  
        


    return
