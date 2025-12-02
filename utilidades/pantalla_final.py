import pygame

from utilidades.fuentes import fuente_diesciseis_bit, fuente_ochobit_in, fuente_ochobit_out
import utilidades.constantes as datos
import utilidades.imagenes as imagen
from funciones.datos_ranking import cargar_datos 

ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

imagen_fondo = imagen.pantalla_derrota
reloj = pygame.time.Clock()

def pantalla_final(puntaje, dificultad):
    ventana.blit(imagen_fondo, (0, 0))

    pygame.mouse.set_visible(True)

    color_activo = pygame.Color((255, 255, 255))
    color_pasivo = pygame.Color((15, 15, 15))
    color = color_pasivo
    estado_input = False
    #fuente = pygame.font.Font(None, 55)
    nombre_usuario = ""
    input_rect = pygame.Rect((datos.ANCHO // 2) - 140, 390, 280, 52)

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
                    if evento.key == pygame.K_RETURN and len(nombre_usuario) > 2 and evento.key != pygame.K_BACKSPACE:
                        #print(nombre_usuario, puntaje, dificultad)
                        cargar_datos(nombre=nombre_usuario, puntaje=puntaje, dificultad=dificultad)
                        iniciar_pantalla = False
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre_usuario = nombre_usuario[:-1]
                    elif len(nombre_usuario) < 10 and evento.key != pygame.K_RETURN and evento.key != pygame.K_BACKSPACE:
                        nombre_usuario += evento.unicode
                    
        
        if estado_input:
            color = color_activo
        else:
            color = color_pasivo

        fin_juego_uno = fuente_ochobit_in.render("FIN DEL JUEGO", True, (255, 0, 0))
        fin_juego_uno_rect = fin_juego_uno.get_rect(center = (datos.ANCHO // 2, 100))

        fin_juego_dos = fuente_ochobit_out.render("FIN DEL JUEGO", True, (30, 30, 30))
        fin_juego_dos_rect = fin_juego_dos.get_rect(center = (datos.ANCHO // 2, 100))

        puntaje_texto = fuente_diesciseis_bit.render(f"Puntaje {puntaje}", True, (255, 255, 255))
        puntaje_texto_rect = puntaje_texto.get_rect(center = (datos.ANCHO / 2, 250))

        nombre_texto = fuente_diesciseis_bit.render("Ingrese su nombre", True, (255, 255, 255))
        nombre_texto_rect = nombre_texto.get_rect(center = (datos.ANCHO / 2, 360))

        ventana.blit(fin_juego_uno, fin_juego_uno_rect)
        ventana.blit(fin_juego_dos, fin_juego_dos_rect)
        ventana.blit(puntaje_texto, puntaje_texto_rect)
        ventana.blit(nombre_texto, nombre_texto_rect)

        pygame.draw.rect(ventana, (20, 20, 20), input_rect)
        superficie_texto = fuente_diesciseis_bit.render(nombre_usuario, True, (240, 240, 240))
        ventana.blit(superficie_texto, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(ventana, color, input_rect, 2)

        #reloj.tick(60)
        pygame.display.update()

    #return 0