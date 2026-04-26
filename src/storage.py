import json
import os

class Storage:
    def __init__(self, filename="tareas.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        # Convertimos objetos a un formato simple (diccionarios) para guardar
        data = [{"title": t.title, "description": t.description, "status": t.status} for t in tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Datos guardados con éxito.")

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        
        with open(self.filename, 'r') as f:
            try:
                data = json.load(f)
                return data # Esto devolverá una lista de diccionarios
            except json.JSONDecodeError:
                return []

