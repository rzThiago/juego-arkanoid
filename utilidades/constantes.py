import pygame
ANCHO = 800
ALTO = 600
TITULO = "Arkaniod - Turbo"
pygame.init()
volumen = 0.5   
dificultad = "facil"
valor_mute = False
fuente = pygame.font.SysFont("fuente/KOMTXT__", 50)
# Botones: texto, rectángulo, y estado de hover previo (para controlar el sonido)

botones = [
    {
        "text": "Play", 
        "rect": pygame.Rect(300, 200, 224, 49), 
        "hover": False, 
        "dimension": {
            "x1":300, "x2":520, "y1":200, "y2":265
        }
    },
    {   "text": "Ranking",
        "rect": pygame.Rect(300, 265, 224, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":330, "y2":330
        }
    },
    {   "text": "Credits",
        "rect": pygame.Rect(300, 395, 224, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":395, "y2":395
        }
    },
    {   "text": "Options", 
        "rect": pygame.Rect(300, 460, 224, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":460, "y2":460
        }
    },
    {   "text": "Exit", 
        "rect": pygame.Rect(300, 525, 224, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":525, "y2":525
        }
    },
    {   
        "text": "Return",
        "rect": pygame.Rect(300, 460, 224, 49),
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":460, "y2":525
        }
    },
    {   "text": "volumen+",
        "rect": pygame.Rect(440, 331, 124, 49), 
        "hover": False,
        "dimension": {
            "x1":440, "x2":560, "y1":331, "y2":395
        }
    },
    {   "text": "volumen-",
        "rect": pygame.Rect(300, 331, 124, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":420, "y1":331, "y2":395
        }
    },
        {   "text": "facil",
        "rect": pygame.Rect(300, 265, 94, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":390, "y1":265, "y2":330
        }
    },
        {   "text": "mediano",
        "rect": pygame.Rect(410, 265, 94, 49), 
        "hover": False,
        "dimension": {
            "x1":410, "x2":500, "y1":265, "y2":330
        }
    },
        {   "text": "dificil",
        "rect": pygame.Rect(520, 265, 94, 49), 
        "hover": False,
        "dimension": {
            "x1":520, "x2":610, "y1":265, "y2":330
        }
    },
    {   "text": "mute",
        "rect": pygame.Rect(300, 395, 224, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":395, "y2":460
        }
    },
        {   "text": "imposible",
        "rect": pygame.Rect(630, 265, 144, 48), 
        "hover": False,
        "dimension": {
            "x1":630, "x2":770, "y1":265, "y2":330
        }
    },
    {   "text": "Continue",
        "rect": pygame.Rect(300, 330, 224, 49), 
        "hover": False,
        "dimension": {
            "x1":300, "x2":520, "y1":265, "y2":330
        }
    }
]