import pygame
import utilidades.constantes as datos
import utilidades.imagenes as imagen
pygame.mixer.init()

ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))
sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")

def valor_de_valumen ():
    
    match datos.volumen:
        case x if datos.volumen <= 0 :
            ventana.blit(imagen.volumen0,(580,350))
        case x if datos.volumen <=0.1 and datos.volumen > 0 :
            ventana.blit(imagen.volumen10,(580,350))
        case x if datos.volumen <=0.2 and datos.volumen > 0.1 :
            ventana.blit(imagen.volumen20,(580,350))
        case x if datos.volumen <=0.3 and datos.volumen > 0.2 :
            ventana.blit(imagen.volumen30,(580,350))
        case x if datos.volumen <=0.4 and datos.volumen > 0.3 :
            ventana.blit(imagen.volumen40,(580,350))
        case x if datos.volumen <=0.5 and datos.volumen > 0.4 :
            ventana.blit(imagen.volumen50,(580,350))
        case x if datos.volumen <=0.6 and datos.volumen > 0.5 :
            ventana.blit(imagen.volumen60,(580,350))
        case x if datos.volumen <=0.7 and datos.volumen > 0.6 :
            ventana.blit(imagen.volumen70,(580,350))
        case x if datos.volumen <=0.8 and datos.volumen > 0.7 :
            ventana.blit(imagen.volumen80,(580,350))
        case x if datos.volumen <=0.9 and datos.volumen > 0.8 :
            ventana.blit(imagen.volumen90,(580,350))
        case x if datos.volumen <=1.1 and datos.volumen > 0.9 :
            ventana.blit(imagen.volumen100,(580,350))
    pygame.display.update()

def mute ():
    sonido_boton.play()
    if datos.valor_mute == False :
        ventana.blit(imagen.activado,(300,415))
        datos.valor_mute = True
        datos.volumen = 0
        pygame.mixer.music.set_volume(datos.volumen)
    else :
        ventana.blit(imagen.desactivado,(300,415))
        datos.valor_mute = False
        datos.volumen = 0.5
        pygame.mixer.music.set_volume(datos.volumen)
    