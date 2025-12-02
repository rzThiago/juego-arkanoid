import json

def cargar_datos(nombre, dificultad, puntaje):
    datos = []
    with open("datos/ranking.json", "r") as archivo:
        datos = json.load(archivo)

    datos_usuario = {"nombre": nombre, "puntaje": puntaje, "dificultad": dificultad}
    datos.append(datos_usuario)
    with open("datos/ranking.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def ordenar_ranking():
    datos = []
    with open("datos/ranking.json", "r") as archivo:
        datos = json.load(archivo)
    
    #bubble sort
    n = len(datos)
    for i in range(n):
        for j in range(n-i-1):
            if datos[j]["puntaje"] <= datos[j + 1]["puntaje"]:
                auxiliar = datos[j + 1]
                datos[j + 1] = datos[j]
                datos[j] = auxiliar
    return datos[:5]