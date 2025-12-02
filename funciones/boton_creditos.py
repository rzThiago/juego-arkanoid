import pygame
import utilidades.constantes as datos
import utilidades.imagenes as imagen
from utilidades.fuentes import fuente_diesciseis_bit, fuente_ochobit_in, fuente_ochobit_out

ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))
pygame.mixer.init()
sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")

def dibujar_creditos():
    sonido_boton.play()
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if datos.botones[5]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    corriendo = False
        
        ventana.blit(imagen.pantalla_creditos, (0, 0))

        ventana.blit(
            imagen.volver,(
                datos.botones[5]["dimension"]["x1"],
                datos.botones[5]["dimension"]["y1"],
                datos.botones[5]["dimension"]["x2"],
                datos.botones[5]["dimension"]["y2"]
                ))

        titulo_creditos_in = fuente_ochobit_in.render("CREDITOS", True, (240, 240, 240))
        titulo_creditos_in_rect = titulo_creditos_in.get_rect(center = (datos.ANCHO / 2, 25))
        titulo_creditos_out = fuente_ochobit_out.render("CREDITOS", True, (0, 0, 0))
        titulo_creditos_out_rect = titulo_creditos_out.get_rect(center = (datos.ANCHO / 2, 25))
        ventana.blit(titulo_creditos_in, titulo_creditos_in_rect)
        ventana.blit(titulo_creditos_out, titulo_creditos_out_rect)

        titulo_desarrolladores = fuente_diesciseis_bit.render("INTEGRANTES", True, (255, 205, 26))
        titulo_musica = fuente_diesciseis_bit.render("MUSICA Y FX", True, (255, 26, 26))
        titulo_arte = fuente_diesciseis_bit.render("ARTE", True, (183, 41, 255))
        ventana.blit(titulo_desarrolladores, (40, 100))
        ventana.blit(titulo_musica, (40, 240))
        ventana.blit(titulo_arte, (40, 380))
    
        nombre_desarrollador_uno = fuente_diesciseis_bit.render("Ezequiel Rodriguez", True, (255, 205, 26))
        nombre_desarrollador_dos = fuente_diesciseis_bit.render("Aaron Pineiro", True, (255, 205, 26))
        nombre_desarrollador_tres = fuente_diesciseis_bit.render("Thiago Rodriguez", True, (255, 205, 26))
        ventana.blit(nombre_desarrollador_uno, (360, 100))
        ventana.blit(nombre_desarrollador_dos, (360, 140))
        ventana.blit(nombre_desarrollador_tres, (360, 180))

        musica_uno = fuente_diesciseis_bit.render("Arkanoid Theme", True, (255, 26, 26))
        musica_dos = fuente_diesciseis_bit.render("Soundimage", True, (255, 26, 26))
        musica_tres = fuente_diesciseis_bit.render("Kenney", True, (255, 26, 26))
        ventana.blit(musica_uno, (360, 240))
        ventana.blit(musica_dos, (360, 280))
        ventana.blit(musica_tres, (360, 320))

        arte_uno = fuente_diesciseis_bit.render("ChatGPT", True, (183, 41, 255))
        arte_dos = fuente_diesciseis_bit.render("Dafont", True, (183, 41, 255))
        ventana.blit(arte_uno, (360, 380))
        ventana.blit(arte_dos, (360, 420))

        pygame.display.flip()
    return
    # Acá podés agregar un título luego:
    # titulo = fuente_titulo.render("CRÉDITOS DEL JUEGO", True, BLANCO)
    # ventana.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
