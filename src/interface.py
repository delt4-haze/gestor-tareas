def show_menu():
    print("\n--- GESTOR DE TAREAS PROFESIONAL ---")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Guardar y Salir")
    return input("Selecciona una opción: ")

def get_task_details():
    title = input("Título de la tarea: ")
    desc = input("Descripción: ")
    return title, desc

