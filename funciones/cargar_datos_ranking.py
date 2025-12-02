import json

def cargar_datos(nombre, dificultad, puntaje):
    datos = {
        "nombre": nombre,
        "dificultad": dificultad,
        "puntaje": puntaje
    }

    with open("utilidades/ranking.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def ordenar_ranking():
    pass