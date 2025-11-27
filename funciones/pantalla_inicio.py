import pygame
import cv2

import utilidades.constantes as datos

pygame.init()

ventana = pygame.display.set_mode((datos.ANCHO, datos.ALTO))

video = cv2.VideoCapture("./utilidades/videos/pantalla_inicio4.mp4")
fps = video.get(cv2.CAP_PROP_FPS)

reloj = pygame.time.Clock()

def pantalla_inicio():
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
        estado_fotograma, fotograma = video.read()
        if estado_fotograma:
            superficie_video = pygame.image.frombuffer(
                fotograma.tobytes(), fotograma.shape[1::-1], "BGR"
            )
        else:
            corriendo = False
        
        reloj.tick(fps)
        ventana.blit(superficie_video, (0, 0))
        pygame.display.flip()