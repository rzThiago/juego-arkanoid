import pygame
import utilidades.constantes as datos
import funciones.funciones as funcion
import funciones.boton_jugar as jugar
import funciones.boton_continuar as continuar
import funciones.boton_creditos as creditos

sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
#sonido_boton.set_volume(datos.volumen)
def principal():
    pygame.mixer.music.load("./utilidades/sonidos/Arkanoid_musica_principal.mp3")
    pygame.mixer.music.play(-1) 
    corriendo = True
    while corriendo:

        funcion.dibujar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for boton in datos.botones:
                    if boton["rect"].collidepoint(pos):
                        if boton["text"] == "Play":
                            jugar.jugar()
                        elif boton["text"] == "Continue":
                            continuar.continuar()
                        elif boton["text"] == "Credits":
                            creditos.creditos()
                        elif boton["text"] == "Options":
                            print("Options...")
                            datos.volumen, datos.dificultad = funcion.dibujar_configuracion()
                            sonido_boton.set_volume(datos.volumen)
                            print(datos.volumen,datos.dificultad)

                        elif boton["text"] == "Exit":
                            sonido_boton.play()
                            corriendo = False

    pygame.quit()