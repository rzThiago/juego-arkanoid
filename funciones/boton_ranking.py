import pygame
import utilidades.constantes as datos
import utilidades.imagenes as imagen
import utilidades.fuentes as fuente
import funciones.funcion_hover as funcion_hover
from utilidades.fuentes import fuente_ochobit_in, fuente_ochobit_out
import json
pygame.mixer.init()
sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

def menu_ranking():
    ventana.blit(imagen.pantalla_configuracion, (0, 0))

    titulo_ranking_in = fuente_ochobit_in.render("RANKING", True, (239, 184, 16))
    titulo_ranking_in_rect = titulo_ranking_in.get_rect(center = (datos.ANCHO // 2, 100))

    titulo_ranking_out = fuente_ochobit_out.render("RANKING", True, (30, 30, 30))
    titulo_ranking_out_rect = titulo_ranking_out.get_rect(center = (datos.ANCHO // 2, 100))

    ventana.blit(titulo_ranking_in, titulo_ranking_in_rect)
    ventana.blit(titulo_ranking_out, titulo_ranking_out_rect)

    ventana.blit(
        imagen.volver,(
            datos.botones[5]["dimension"]["x1"],
            datos.botones[5]["dimension"]["y1"],
            datos.botones[5]["dimension"]["x2"],
            datos.botones[5]["dimension"]["y2"]
            ))
    funcion_hover.funcion_hover(5)

    with open("utilidades/ranking.json", "r") as archivo:
        ranking = json.load(archivo)  # Cargar el contenido del archivo JSON
        print(f"Ranking: {ranking}")
    fuente = datos.fuente
    
    prueba = {"Carla": 500000}
    ranking.update(prueba)
    contador =0
    
    for clave, valor in ranking.items():
        texto = fuente.render(clave, True, (255, 255, 0)) 
        ventana.blit(texto, (250, 200 + 30*contador))
        texto = fuente.render(str(valor), True, (255, 255, 0)) 
        ventana.blit(texto, (450, 200 + 30*contador))
         
        print(f"Nombre: {clave}, Edad: {valor}")
        contador += 1
    
    pygame.display.update()
def ranking():
    sonido_boton.play() 
    corriendo = True
    while corriendo:
        menu_ranking()
        for evento in pygame.event.get():
            pygame.mixer.music.set_volume(datos.volumen) 
            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if datos.botones[5]["rect"].collidepoint(pos):
                    sonido_boton.play()

                    print("Click en Return")
                    return
    
    #with open("utilidades/ranking.json", "w", encoding="utf-8") as archivo:
    #    json.dump(ranking, archivo, indent=4, ensure_ascii=False)












































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