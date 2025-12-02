import pygame
import json

import utilidades.constantes as constantes
import utilidades.imagenes as imagen
import utilidades.fuentes as fuente
import funciones.funcion_hover as funcion_hover
from utilidades.fuentes import fuente_ochobit_in, fuente_ochobit_out, fuente_diesciseis_bit
from funciones.datos_ranking import ordenar_ranking
pygame.mixer.init()
sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

def menu_ranking():
    sonido_boton.play()

    datos = []
    with open("datos/ranking.json", "r") as archivo:
        datos = json.load(archivo)  # Cargar el contenido del archivo JSON

    ranking_usuarios = ordenar_ranking()
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            pygame.mixer.music.set_volume(constantes.volumen) 
            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if constantes.botones[5]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    return
        ventana.blit(imagen.pantalla_ranking, (0, 0))

        titulo_ranking_in = fuente_ochobit_in.render("RANKING", True, (239, 184, 16))
        titulo_ranking_in_rect = titulo_ranking_in.get_rect(center = (constantes.ANCHO // 2, 50))

        titulo_ranking_out = fuente_ochobit_out.render("RANKING", True, (30, 30, 30))
        titulo_ranking_out_rect = titulo_ranking_out.get_rect(center = (constantes.ANCHO // 2, 50))

        ventana.blit(titulo_ranking_in, titulo_ranking_in_rect)
        ventana.blit(titulo_ranking_out, titulo_ranking_out_rect)

        ventana.blit(
            imagen.volver,(
                constantes.botones[5]["dimension"]["x1"],
                constantes.botones[5]["dimension"]["y1"],
                constantes.botones[5]["dimension"]["x2"],
                constantes.botones[5]["dimension"]["y2"]
                ))
        funcion_hover.funcion_hover(5)
        
        titulo_posicion = fuente_diesciseis_bit.render("POS", True, (54, 242, 255))
        titulo_nombre = fuente_diesciseis_bit.render("NOMBRE", True, (20, 222, 73))
        titulo_puntos = fuente_diesciseis_bit.render("PUNTOS", True, (245, 54, 255))
        titulo_dificultad = fuente_diesciseis_bit.render("DIFICULTAD", True, (245, 32, 32))
        ventana.blit(titulo_posicion, (25, 150))
        ventana.blit(titulo_nombre, (150, 150))
        ventana.blit(titulo_puntos, (380, 150))
        ventana.blit(titulo_dificultad, (560, 150))

        posicion_uno = fuente_diesciseis_bit.render("1", True, (255, 255, 255))
        posicion_dos = fuente_diesciseis_bit.render("2", True, (255, 255, 255))
        posicion_tres = fuente_diesciseis_bit.render("3", True, (255, 255, 255))
        posicion_cuatro = fuente_diesciseis_bit.render("4", True, (255, 255, 255))
        posicion_cinco = fuente_diesciseis_bit.render("5", True, (255, 255, 255))
        ventana.blit(posicion_uno, (50, 200))
        ventana.blit(posicion_dos, (50, 245))
        ventana.blit(posicion_tres, (50, 290))
        ventana.blit(posicion_cuatro, (50, 335))
        ventana.blit(posicion_cinco, (50, 380))

        #prueba = {"Carla": 500000}
        #ranking.update(prueba)
        contador = 0
        for dato in ranking_usuarios:
            texto_nombre = fuente_diesciseis_bit.render(dato["nombre"], True, (255, 255, 255)) 
            ventana.blit(texto_nombre, (130, 200 + 30*contador))

            texto_puntaje = fuente_diesciseis_bit.render(str(dato["puntaje"]), True, (255, 255, 255)) 
            ventana.blit(texto_puntaje, (410, 200 + 30*contador))

            texto_dificultad = fuente_diesciseis_bit.render(dato["dificultad"], True, (255, 255, 255)) 
            ventana.blit(texto_dificultad, (595, 200 + 30*contador))
            
            contador += 1.5
        
        pygame.display.update()














































    """
    sonido_boton.set_volume(datos.volumen)
    sonido_boton.play()
    print("Creditos...")
    print(f"Dificultad = {datos.dificultad} Volumen = {datos.volumen}")
    """
    """
    
    # con context manager y uso de load
        with open("archivos/datos.json", "r") as archivo:
            datos = json.load(archivo)  # Cargar el contenido del archivo JSON

    # Ahora 'datos' contiene el contenido del archivo JSON como un diccionario de Python
    print(datos)

    # la diferencia entre json.load() y json.loads() está en el tipo de fuente desde donde se lee el JSON:
    # - json.load()
    #   Espera un objeto tipo archivo (como el que se obtiene con open()).
    #   Se usa cuando vamos a leer JSON desde un archivo real.
    # - json.loads()
    #   Espera un string de texto que contenga JSON.
    #   Se usa cuando tenemos el contenido JSON en una cadena (por ejemplo, descargado de internet o leído desde otro formato). 
    """
    # metodo update
    """ usuario = {'nombre': 'Alice', 'edad': 30}
    nuevos_datos = {'edad': 31, 'profesion': 'Ingeniera'}

    usuario.update(nuevos_datos)

    print(usuario) """