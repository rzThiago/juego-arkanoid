import pygame

from utilidades.fuentes import fuente_principal, fuente_ocho_bit
import utilidades.constantes as datos
import utilidades.imagenes as imagen


imagen_fondo = imagen.pantalla_derrota

def pantalla_final(ventana, puntaje, dificultad):
    ventana.blit(imagen_fondo, (0, 0))

    color_activo = pygame.Color((255, 255, 255))
    color_pasivo = pygame.Color((15, 15, 15))
    color = color_pasivo
    estado_input = False
    fuente = pygame.font.Font(None, 55)
    nombre_usuario = ""
    input_rect = pygame.Rect((800 // 2) - 250, 380, 500, 60)

    iniciar_pantalla = True
    while iniciar_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(evento.pos):
                    estado_input = True
                else:
                    estado_input = False

            if evento.type == pygame.KEYDOWN:
                if estado_input == True:
                    if evento.key == pygame.K_RETURN and len(nombre_usuario) > 2:
                        print(nombre_usuario, puntaje, dificultad)
                        iniciar_pantalla = False
                        return 0
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre_usuario = nombre_usuario[:-1]
                    elif len(nombre_usuario) < 16 and evento.key != pygame.K_RETURN:
                        nombre_usuario += evento.unicode
                    
        
        if estado_input:
            color = color_activo
        else:
            color = color_pasivo

        render1 = fuente_ocho_bit.render("FIN DEL JUEGO", True, (255, 255, 255))
        render2 = fuente_principal.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
        render3 = fuente_principal.render("Nombre:", True, (255, 255, 255))
        ventana.blit(render1, (320, 100))
        ventana.blit(render2, (320, 250))
        ventana.blit(render3, (320, 330))
        pygame.draw.rect(ventana, color, input_rect, 2)
        superficie_texto = fuente.render(nombre_usuario, True, (240, 240, 240))
        ventana.blit(superficie_texto, (input_rect.x + 5, input_rect.y +5))
        pygame.display.flip()