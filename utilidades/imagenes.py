import pygame


# Cargamos el fondo
pantalla_principal = pygame.image.load("./utilidades/imagenes/pantalla_principal1.png")
pantalla_creditos = pygame.image.load("./utilidades/imagenes/pantalla_creditos.png")

pantalla_configuracion = pygame.image.load("./utilidades/imagenes/pantalla_configuracion31.png")
# Reescalamos la Imagen de fondo
#pantalla_principal = pygame.transform.scale(pantalla_principal, (800, 600))

pantalla_configuracion = pygame.transform.scale(pantalla_configuracion, (800, 600))
pantalla_creditos = pygame.transform.scale(pantalla_creditos, (800, 600))

pantalla_derrota = pygame.image.load("./utilidades/imagenes/pantalla_derrota2.png")
#pantalla_derrota = pygame.transform.scale(pantalla_derrota, (800, 600))

pantalla_pausa = pygame.image.load("./utilidades/imagenes/pantalla_pausa2.png")
pantalla_configuracion = pygame.image.load("./utilidades/imagenes/pantalla_configuracion31.png")
pantalla_derrota = pygame.image.load("./utilidades/imagenes/pantalla_derrota2.png")
pantalla_juego = pygame.image.load("./utilidades/imagenes/fondo_juego.png")
pantalla_ranking = pygame.image.load("./utilidades/imagenes/pantalla_ranking1.png")
# Reescalamos la Imagen de fondo
#pantalla_pausa = pygame.transform.scale(pantalla_pausa, (800, 600))

#pantalla_derrota = pygame.transform.scale(pantalla_derrota, (800, 600))
pantalla_principal = pygame.transform.scale(pantalla_principal, (800, 600))
pantalla_configuracion = pygame.transform.scale(pantalla_configuracion, (800, 600))
pantalla_ranking = pygame.transform.scale(pantalla_ranking, (800, 600))
#Cargamos imagenes
jugar = pygame.image.load("./utilidades/imagenes/Play1.png")
continuar = pygame.image.load("./utilidades/imagenes/Continue1.png")
creditos = pygame.image.load("./utilidades/imagenes/Credits1.png")
opciones = pygame.image.load("./utilidades/imagenes/Options1.png")
volver = pygame.image.load("./utilidades/imagenes/Return1.png")
salir = pygame.image.load("./utilidades/imagenes/Exit1.png")
sumar_volumen = pygame.image.load("./utilidades/imagenes/volumen+1.png")
restar_volumen = pygame.image.load("./utilidades/imagenes/volumen-1.png")
facil = pygame.image.load("./utilidades/imagenes/Facil1.png")
mediano = pygame.image.load("./utilidades/imagenes/Medium1.png")
dificil = pygame.image.load("./utilidades/imagenes/Hard1.png")
dificultad= pygame.image.load("./utilidades/imagenes/Dificultad1.png")
volumen = pygame.image.load("./utilidades/imagenes/volumen1.png")
mute = pygame.image.load("./utilidades/imagenes/mute1.png")
activado = pygame.image.load("./utilidades/imagenes/activado1.png")
desactivado = pygame.image.load("./utilidades/imagenes/desactivado1.png")
imposible = pygame.image.load("./utilidades/imagenes/imposible1.png")
volumen0 = pygame.image.load("./utilidades/imagenes/volumen01.png")
volumen10 = pygame.image.load("./utilidades/imagenes/volumen101.png")
volumen20 = pygame.image.load("./utilidades/imagenes/volumen201.png")
volumen30 = pygame.image.load("./utilidades/imagenes/volumen301.png")
volumen40 = pygame.image.load("./utilidades/imagenes/volumen401.png")
volumen50 = pygame.image.load("./utilidades/imagenes/volumen501.png")
volumen60 = pygame.image.load("./utilidades/imagenes/volumen601.png")
volumen70 = pygame.image.load("./utilidades/imagenes/volumen701.png")
volumen80 = pygame.image.load("./utilidades/imagenes/volumen801.png")
volumen90 = pygame.image.load("./utilidades/imagenes/volumen901.png")
volumen100 = pygame.image.load("./utilidades/imagenes/volumen1001.png")
ranking= pygame.image.load("./utilidades/imagenes/Ranking1.png")


nave_enemiga_original = pygame.image.load("./utilidades/imagenes/Nave alien sin fondo.png")
nave_enemiga = pygame.transform.scale(nave_enemiga_original, (60,40))

sprite_rojo_original = pygame.image.load("./utilidades/imagenes/Alien rojo transparente.png")
sprite_alien_rojo = pygame.transform.scale(sprite_rojo_original, (60,40))

sprite_verde_original = pygame.image.load("./utilidades/imagenes/Alien verde.png") 
sprite_alien_verde = pygame.transform.scale(sprite_verde_original, (60,34))

sprite_azul_original = pygame.image.load("./utilidades/imagenes/Alien Azul.png")
sprite_alien_azul = pygame.transform.scale(sprite_azul_original, (60,40))

sprite_amarillo_original = pygame.image.load("./utilidades/imagenes/Alien Amarillo sin fondo.png")
sprite_alien_amarillo = pygame.transform.scale(sprite_amarillo_original, (60,40))

milenario_original = pygame.image.load("./utilidades/imagenes/Halcon sin fondo.png")
sprite_milenario = pygame.transform.scale(milenario_original, (100,45))

sprite_explosion = pygame.image.load("./utilidades/imagenes/Explosion.png")

bolita_original= pygame.image.load("./utilidades/imagenes/Bala  Pelotita.png")
sprite_bolita = pygame.transform.scale(bolita_original, (15,15))

icono = pygame.image.load("./utilidades/imagenes/icono.png")