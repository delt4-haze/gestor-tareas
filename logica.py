import json
import os

ARCHIVO = "data.json"

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)
