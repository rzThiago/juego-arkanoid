import pygame
import utilidades.constantes as datos
import utilidades.imagenes as imagen
import funciones.funcion_volumen as valor_volumen
#from utilidades.fuentes import fuente_principal

pygame.mixer.init()

ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))
sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
def dibujar_menu():
    #fuente_principal = pygame.font.SysFont(None, 50)
    ventana.blit(imagen.pantalla_principal, (0, 0))

    for boton in datos.botones:

        ventana.blit(
            imagen.jugar,(
                datos.botones[0]["dimension"]["x1"],
                datos.botones[0]["dimension"]["y1"],
                datos.botones[0]["dimension"]["x2"],
                datos.botones[0]["dimension"]["y2"]
        ))
        ventana.blit(
            imagen.continuar,(
                datos.botones[1]["dimension"]["x1"],
                datos.botones[1]["dimension"]["y1"],
                datos.botones[1]["dimension"]["x2"],
                datos.botones[1]["dimension"]["y2"]
        ))
        ventana.blit(
            imagen.creditos,(
                datos.botones[2]["dimension"]["x1"],
                datos.botones[2]["dimension"]["y1"],
                datos.botones[2]["dimension"]["x2"],
                datos.botones[2]["dimension"]["y2"]
        ))
        ventana.blit(
            imagen.opciones,(
                datos.botones[3]["dimension"]["x1"],
                datos.botones[3]["dimension"]["y1"],
                datos.botones[3]["dimension"]["x2"],
                datos.botones[3]["dimension"]["y2"]
        ))
        ventana.blit(
            imagen.salir,(
                datos.botones[4]["dimension"]["x1"],
                datos.botones[4]["dimension"]["y1"],
                datos.botones[4]["dimension"]["x2"],
                datos.botones[4]["dimension"]["y2"]
        ))
        ventana.blit(
            imagen.ranking,(
                datos.botones[13]["dimension"]["x1"],
                datos.botones[13]["dimension"]["y1"],
                datos.botones[13]["dimension"]["x2"],
                datos.botones[13]["dimension"]["y2"]
        ))
    pygame.display.update()

def dibujar_configuracion():
    ventana.blit(imagen.pantalla_configuracion, (0, 0))

    sonido_boton.set_volume(datos.volumen)
    sonido_boton.play()
    ventana.blit(imagen.dificultad,(120,265))
    ventana.blit(imagen.volumen,(120,331))
    ventana.blit(imagen.desactivado,(300,395))
    ventana.blit(imagen.mute,(120,395))

    ventana.blit(
        imagen.volver,(
            datos.botones[5]["dimension"]["x1"],
            datos.botones[5]["dimension"]["y1"],
            datos.botones[5]["dimension"]["x2"],
            datos.botones[5]["dimension"]["y2"]
            ))
    ventana.blit(
        imagen.sumar_volumen,(
            datos.botones[6]["dimension"]["x1"],
            datos.botones[6]["dimension"]["y1"],
            datos.botones[6]["dimension"]["x2"],
            datos.botones[6]["dimension"]["y2"]
            ))
    ventana.blit(
        imagen.restar_volumen,(
            datos.botones[7]["dimension"]["x1"],
            datos.botones[7]["dimension"]["y1"],
            datos.botones[7]["dimension"]["x2"],
            datos.botones[7]["dimension"]["y2"]
            ))
    ventana.blit(
        imagen.facil,(
            datos.botones[8]["dimension"]["x1"],
            datos.botones[8]["dimension"]["y1"],
            datos.botones[8]["dimension"]["x2"],
            datos.botones[8]["dimension"]["y2"]
            ))
    ventana.blit(
        imagen.mediano,(
            datos.botones[9]["dimension"]["x1"],
            datos.botones[9]["dimension"]["y1"],
            datos.botones[9]["dimension"]["x2"],
            datos.botones[9]["dimension"]["y2"]
            ))
    ventana.blit(
        imagen.dificil,(
            datos.botones[10]["dimension"]["x1"],
            datos.botones[10]["dimension"]["y1"],
            datos.botones[10]["dimension"]["x2"],
            datos.botones[10]["dimension"]["y2"]
            ))
    ventana.blit(
        imagen.imposible,(
            datos.botones[12]["dimension"]["x1"],
            datos.botones[12]["dimension"]["y1"],
            datos.botones[12]["dimension"]["x2"],
            datos.botones[12]["dimension"]["y2"]
            ))
    
    pygame.display.update()
    
    corriendo = True
    while (True):   
        valor_volumen.valor_de_valumen()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            pygame.mixer.music.set_volume(datos.volumen) 
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if datos.botones[5]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    print("Click en Return")
                    print(f"Volumen = {datos.volumen}")
                    return datos.volumen, datos.dificultad
                if datos.botones[6]["rect"].collidepoint(pos):
                    if datos.valor_mute == False :
                        if (datos.volumen <= 1):
                            datos.volumen += .1
                        print(f"Volumen = {datos.volumen}")
                        sonido_boton.set_volume(datos.volumen)
                        sonido_boton.play()
                        print("Click en volumen +")

                if datos.botones[7]["rect"].collidepoint(pos):
                    if datos.valor_mute == False :
                        if (datos.volumen >=0):
                            datos.volumen -= 0.1
                        print(f"Volumen = {datos.volumen}")
                        sonido_boton.set_volume(datos.volumen)
                        sonido_boton.play()
                        print("Click en volumen -")
                if datos.botones[8]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    datos.dificultad = "facil"
                if datos.botones[9]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    datos.dificultad = "medio"
                if datos.botones[10]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    datos.dificultad = "dificil"
                if datos.botones[11]["rect"].collidepoint(pos):
                    valor_volumen.mute()
                if datos.botones[12]["rect"].collidepoint(pos):
                    sonido_boton.play()
                    datos.dificultad = "imposible"


