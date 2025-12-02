import pygame
import utilidades.imagenes as imagen

pygame.init()
ventana = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont(None, 60)
def introduccion():
    ventana.blit(imagen.pantalla_principal, (0, 0))
    lineas=[
    "Hace 200 años, una fuerza oscura despertó...",
    "Nadie pudo detenerla.",
    "Ahora, el destino está en tus manos."
    ]
    font = pygame.font.SysFont(None, 40)
    y = 200
    
    for linea in lineas:
        pantalla = True
        while pantalla:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    showing = False
            
            ventana.blit(imagen.pantalla_principal, (0, 0))
            texto = font.render(linea, True, (255, 255, 255))
            ventana.blit(texto, (50, y))
            pygame.display.update()
            pygame.time.delay(1200)

            pantalla = False
        y += 50
