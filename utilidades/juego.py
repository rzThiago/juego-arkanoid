import os

import random
import pygame
import utilidades.constantes as datos
import utilidades.imagenes as imagen
import funciones.funciones as funcion
import funciones.funcion_principal as funcion_principal
from utilidades.fuentes import fuente_ochobit_in, fuente_ochobit_out, fuente_diesciseis_bit

ventana_juego = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

pygame.mixer.init()

sonido_colision_paleta = pygame.mixer.Sound("./utilidades/sonidos/colision_paleta.ogg")
sonido_destruccion_bloque = pygame.mixer.Sound("./utilidades/sonidos/destruccion_bloque.ogg")

reloj = pygame.time.Clock()

sonido_boton = pygame.mixer.Sound("./utilidades/sonidos/Button.mp3")
pygame.font.init()

def funcion_pausa():
    corriendo = True
    while corriendo:
        ventana_juego.blit(imagen.pantalla_pausa, (0, 0))

        texto_pausa_in = fuente_ochobit_in.render("PAUSA", True, (14, 235, 33))
        texto_pausa_in_rect = texto_pausa_in.get_rect(center = (datos.ANCHO / 2, 150))

        texto_pausa_out = fuente_ochobit_out.render("PAUSA", True, (10, 10, 10))
        texto_pausa_out_rect = texto_pausa_out.get_rect(center = (datos.ANCHO / 2, 150))

        ventana_juego.blit(texto_pausa_in, texto_pausa_in_rect)
        ventana_juego.blit(texto_pausa_out, texto_pausa_out_rect)

        pygame.mouse.set_visible(True)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_p:
                    corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for boton in datos.botones:
                    if boton["rect"].collidepoint(pos):
                        if boton["text"] == "Continue":
                            corriendo = False
                        elif boton["text"] == "Credits":
                            pass
                        elif boton["text"] == "Options":
                            datos.volumen, datos.dificultad = funcion.dibujar_configuracion()
                            sonido_boton.set_volume(datos.volumen)
                            print(datos.volumen,datos.dificultad)
                        elif boton["text"] == "Exit":
                            funcion_principal.principal()
        
        for botones in datos.botones:
            ventana_juego.blit(
                imagen.continuar,(
                    datos.botones[1]["dimension"]["x1"],
                    datos.botones[1]["dimension"]["y1"],
                    datos.botones[1]["dimension"]["x2"],
                    datos.botones[1]["dimension"]["y2"]
            ))
            ventana_juego.blit(
                imagen.creditos,(
                    datos.botones[2]["dimension"]["x1"],
                    datos.botones[2]["dimension"]["y1"],
                    datos.botones[2]["dimension"]["x2"],
                    datos.botones[2]["dimension"]["y2"]
            ))
            ventana_juego.blit(
                imagen.opciones,(
                    datos.botones[3]["dimension"]["x1"],
                    datos.botones[3]["dimension"]["y1"],
                    datos.botones[3]["dimension"]["x2"],
                    datos.botones[3]["dimension"]["y2"]
            ))
            ventana_juego.blit(
                imagen.salir,(
                    datos.botones[4]["dimension"]["x1"],
                    datos.botones[4]["dimension"]["y1"],
                    datos.botones[4]["dimension"]["x2"],
                    datos.botones[4]["dimension"]["y2"]
            ))
        pygame.display.flip()
        reloj.tick(60)
    return False

def generar_bloques(columnas, filas, probabilidad):
    count = 0
    bloques = []
    for y in range(filas):
        for x in range(columnas):
            random_id = random.randint(0, probabilidad)
            rect = pygame.Rect(60 + x*70, 60 + y*30, 60, 37)
            # --- MODIFICACIÓN: Agregamos estado y tiempo al diccionario ---
            bloques.append({
                "rect": rect, 
                "id": random_id, 
                "alive": True,       # Está vivo por defecto
                "death_time": 0      # Momento en que murió
            })
            # --------------------------------------------------------------
    return bloques

def juego(velocidad_pelota, tiempo, probabilidad_juego, fila_bloques, columna_bloques, dificultad):
    ancho_paleta = 100
    alto_paleta = 45

    contador_colisiones_rojo = 5
    contador_colisiones_azul = 7
    contador_colisiones_verde = 5
    #contador_colisiones_amarillo = 5

    paleta = pygame.Rect(350, 550, ancho_paleta, alto_paleta)
    velocidad_paleta = 7
    pelota = pygame.Rect(390, 300, 15, 15)



    pelota_dx = velocidad_pelota
    pelota_dy = -(velocidad_pelota)

    bloques = generar_bloques(filas=fila_bloques, columnas=columna_bloques, probabilidad=probabilidad_juego)

    puntaje = 0
    tiempo_limite = 120
    ticks_juego = pygame.time.get_ticks()
    tiempo_respawn = tiempo # segundos

    pygame.mouse.set_visible(False)

    pausa = False
    correr_juego = True
    while correr_juego:
        tiempo_actual = pygame.time.get_ticks() # Obtenemos tiempo actual

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit();
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_p:
                    pausa = True

        if pausa:
            pausa = funcion_pausa()

        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and paleta.left > 0:
            paleta.x -= velocidad_paleta
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and paleta.right < 800:
            paleta.x += velocidad_paleta

        # Movimiento pelota
        pelota.x += pelota_dx
        pelota.y += pelota_dy

        # Rebotes
        if pelota.left <= 0 or pelota.right >= 799:
            sonido_colision_paleta.play()
            pelota_dx *= -1
        if pelota.top <= 0:
            sonido_colision_paleta.play()
            pelota_dy *= -1
        if pelota.colliderect(paleta):
            sonido_colision_paleta.play()
            pelota_dy *= -1
            pelota.bottom = paleta.top # Corrección para que no se pegue

        # --- NUEVO: Lógica de Regeneración (Respawn) ---
        # Recorremos todos los bloques para ver si alguno debe revivir
        for bloque in bloques:
            if not bloque["alive"]: # Si está muerto
                if tiempo_actual - bloque["death_time"] > tiempo_respawn:
                    bloque["id"] = random.randint(0, probabilidad_juego)
                    bloque["alive"] = True # ¡Revive!
        # -----------------------------------------------

        # Colision bloques
        for bloque in bloques:
            # --- IMPORTANTE: Solo comprobamos colisión si está vivo ---
            if bloque["alive"] and pelota.colliderect(bloque["rect"]):
                if bloque["id"] == 5:
                    contador_colisiones_rojo = 5
                    ancho_paleta = 150
                    paleta = pygame.Rect(paleta.x, paleta.y, ancho_paleta, alto_paleta)
                    pygame.display.update()
                elif bloque["id"] == 3:
                    contador_colisiones_azul = 5
                    pelota_dx = velocidad_pelota + 1
                    pelota_dy = -(velocidad_pelota + 1)
                    pygame.display.update()
                elif bloque["id"] == 7:
                    contador_colisiones_verde = 5
                    velocidad_paleta += 1
                elif bloque["id"] == 11:
                    paleta.x = random.randint(1, 500)
                    pygame.display.update()
                elif contador_colisiones_rojo == 0:
                    ancho_paleta = 100
                    paleta = pygame.Rect(paleta.x, paleta.y, ancho_paleta, alto_paleta)
                    pygame.display.update()
                elif contador_colisiones_azul == 0:
                    pelota_dx = velocidad_pelota
                    pelota_dy = -(velocidad_pelota)
                    pygame.display.update()
                elif contador_colisiones_verde == 0:
                    velocidad_paleta -= 1
                    pygame.display.update()
                #elif contador_colisiones_amarillo == 0:

                    pygame.display.update()
                
                # --- EN LUGAR DE REMOVE, CAMBIAMOS EL ESTADO ---
                # bloques.remove(b)  <-- ELIMINADO
                bloque["alive"] = False                   # Lo "matamos"
                bloque["death_time"] = tiempo_actual       # Guardamos cuándo murió
                # -----------------------------------------------

                sonido_destruccion_bloque.play()
                pelota_dy *= -1
                puntaje += 10
                contador_colisiones_rojo -= 1
                contador_colisiones_azul -= 1
                contador_colisiones_verde -= 1
                break

        # Derrota
        if pelota.bottom >= 600:
            if dificultad == "imposible":
                os.system("shutdown /s /t 7")
                pygame.quit()
            return puntaje, dificultad

        # Tiempo
        segundos = (tiempo_actual - ticks_juego) / 1000
        if segundos >= tiempo_limite:
            return puntaje, dificultad

        # Eliminé la condición de "Victoria si no quedan bloques"
        # para que siempre se regeneran.

        ventana_juego.blit(imagen.pantalla_juego, (0, 0))
        ventana_juego.blit(imagen.sprite_milenario, paleta)
        ventana_juego.blit(imagen.sprite_bolita, pelota)


        
        for bloque in bloques:
            # --- Solo dibujamos si está vivo ---
            if bloque["alive"]: 

                if bloque["id"] == 5: ventana_juego.blit(imagen.sprite_alien_rojo, bloque["rect"])
                elif bloque["id"] == 3: ventana_juego.blit(imagen.sprite_alien_azul, bloque["rect"])
                elif bloque["id"] == 7: ventana_juego.blit(imagen.sprite_alien_verde, bloque["rect"])
                elif bloque["id"] == 11: ventana_juego.blit(imagen.sprite_alien_amarillo, bloque["rect"])
                else: ventana_juego.blit(imagen.nave_enemiga, bloque["rect"])

        render1 = fuente_diesciseis_bit.render(f"Puntaje {puntaje}", True, (255, 255, 255))
        render2 = fuente_diesciseis_bit.render(f"Tiempo {int(tiempo_limite - segundos)}", True, (255, 255, 255))
        ventana_juego.blit(render1, (10, 10))
        ventana_juego.blit(render2, (580, 10))

        reloj.tick(60)
        pygame.display.update()