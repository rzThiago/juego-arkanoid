import os

import random
import pygame

pygame.mixer.init()

sonido_colision_paleta = pygame.mixer.Sound("./utilidades/sonidos/colision_paleta.ogg")
sonido_destruccion_bloque = pygame.mixer.Sound("./utilidades/sonidos/destruccion_bloque.ogg")

reloj = pygame.time.Clock()

pygame.font.init()
fuente = pygame.font.SysFont("Arial", 28)

def generar_bloques(columnas, filas, probabilidad):
    count = 0
    bloques = []
    for y in range(filas):
        for x in range(columnas):
            random_id = random.randint(0, probabilidad)
            rect = pygame.Rect(60 + x*70, 60 + y*30, 60, 20)
            # --- MODIFICACIÓN: Agregamos estado y tiempo al diccionario ---
            bloques.append({
                "rect": rect, 
                "id": random_id, 
                "alive": True,       # Está vivo por defecto
                "death_time": 0      # Momento en que murió
            })
            # --------------------------------------------------------------
    return bloques

def juego(ventana_juego, velocidad_pelota, tiempo, probabilidad_juego, fila_bloques, columna_bloques, dificultad):
    ancho_paleta = 100
    alto_paleta = 15
    contador_colisiones_rojo = 5
    contador_colisiones_azul = 5

    paleta = pygame.Rect(350, 550, ancho_paleta, alto_paleta)
    pelota = pygame.Rect(390, 300, 15, 15)

    pelota_dx = velocidad_pelota
    pelota_dy = -(velocidad_pelota)

    bloques = generar_bloques(filas=fila_bloques, columnas=columna_bloques, probabilidad=probabilidad_juego)

    puntaje = 0
    tiempo_limite = 120
    ticks_juego = pygame.time.get_ticks()
    tiempo_respawn = tiempo # segundos

    correr_juego = True
    while correr_juego:
        tiempo_actual = pygame.time.get_ticks() # Obtenemos tiempo actual

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit();

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and paleta.left > 0:
            paleta.x -= 7
        if teclas[pygame.K_RIGHT] and paleta.right < 800:
            paleta.x += 7

        # Movimiento pelota
        pelota.x += pelota_dx
        pelota.y += pelota_dy

        # Rebotes
        if pelota.left <= 0 or pelota.right >= 800:
            pelota_dx *= -1
        if pelota.top <= 0:
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
                elif contador_colisiones_rojo == 0:
                    ancho_paleta = 100
                    paleta = pygame.Rect(paleta.x, paleta.y, ancho_paleta, alto_paleta)
                    pygame.display.update()
                elif contador_colisiones_azul == 0:
                    pelota_dx = velocidad_pelota
                    pelota_dy = -(velocidad_pelota)
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
                break

        # Derrota
        if pelota.bottom >= 600:
            if dificultad == "imposible":
                os.system("shutdown /s /t 5")
                pygame.quit()
            return puntaje, dificultad

        # Tiempo
        segundos = (tiempo_actual - ticks_juego) / 1000
        if segundos >= tiempo_limite:
            return puntaje, dificultad

        # Eliminé la condición de "Victoria si no quedan bloques"
        # porque siempre se regeneran.

        ventana_juego.fill((10, 10, 10))

        pygame.draw.rect(ventana_juego, (200,200,200), paleta)
        pygame.draw.ellipse(ventana_juego, (255,255,255), pelota)
        
        for bloque in bloques:
            # --- Solo dibujamos si está vivo ---
            if bloque["alive"]: 
                if bloque["id"] == 5: pygame.draw.rect(ventana_juego, (69, 21, 13), bloque["rect"])
                elif bloque["id"] == 3: pygame.draw.rect(ventana_juego, (23, 20, 100), bloque["rect"])
                else: pygame.draw.rect(ventana_juego, (250, 250, 250), bloque["rect"])

        render1 = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
        render2 = fuente.render(f"Tiempo: {int(tiempo_limite - segundos)}", True, (255, 255, 255))
        ventana_juego.blit(render1, (10, 10))
        ventana_juego.blit(render2, (650, 10))

        reloj.tick(60)
        pygame.display.update()