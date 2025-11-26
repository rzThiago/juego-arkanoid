import pygame
ANCHO = 800
ALTO = 600
TITULO = "Arkaniod - Turbo"

volumen = 0.5   
dificultad = "facil"
valor_mute = False
# Botones: texto, rectángulo, y estado de hover previo (para controlar el sonido)

botones = [
    {
        "text": "Play", 
        "rect": pygame.Rect(300, 220, 220, 45), 
        "hover": False, 
        "dimension": {
            "x1":300, "x2":520, "y1":220, "y2":265
        }
    },
    {   "text": "Continue",
        "rect": pygame.Rect(300, 285, 220, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":285, "y2":330
        }
    },
    {   "text": "Credits",
        "rect": pygame.Rect(300, 350, 220, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":350, "y2":395
        }
    },
    {   "text": "Options", 
        "rect": pygame.Rect(300, 415, 220, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":415, "y2":460
        }
    },
    {   "text": "Exit", 
        "rect": pygame.Rect(300, 480, 220, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":480, "y2":525
        }
    },
    {   
        "text": "Return",
        "rect": pygame.Rect(300, 480, 220, 45),
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":480, "y2":525
        }
    },
    {   "text": "volumen+",
        "rect": pygame.Rect(440, 350, 120, 45), 
        "hover": False,
        "dimension": {
            "x1":440, "x2":560, "y1":350, "y2":395
        }
    },
    {   "text": "volumen-",
        "rect": pygame.Rect(300, 350, 120, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":420, "y1":350, "y2":395
        }
    },
        {   "text": "facil",
        "rect": pygame.Rect(300, 285, 90, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":390, "y1":285, "y2":330
        }
    },
        {   "text": "mediano",
        "rect": pygame.Rect(410, 285, 90, 45), 
        "hover": False,
        "dimension": {
            "x1":410, "x2":500, "y1":285, "y2":330
        }
    },
        {   "text": "dificil",
        "rect": pygame.Rect(520, 285, 90, 45), 
        "hover": False,
        "dimension": {
            "x1":520, "x2":610, "y1":285, "y2":330
        }
    },
    {   "text": "mute",
        "rect": pygame.Rect(300, 415, 220, 45), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":415, "y2":460
        }
    },
        {   "text": "imposible",
        "rect": pygame.Rect(630, 285, 140, 45), 
        "hover": False,
        "dimension": {
            "x1":630, "x2":770, "y1":285, "y2":330
        }
    }


]