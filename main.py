from src.task_logic import TaskManager
from src.storage import Storage
from src.interface import show_menu, get_task_details

def main():
    manager = TaskManager()
    storage = Storage()

    # Cargamos tareas previas si existen
    saved_data = storage.load_tasks()
    # (Aquí podrías agregar lógica para convertir los dicts guardados en objetos Task de nuevo)

    while True:
        choice = show_menu()
        
        if choice == "1":
            title, desc = get_task_details()
            manager.add_task(title, desc)
        elif choice == "2":
            print(manager.list_tasks())
        elif choice == "3":
            storage.save_tasks(manager.get_all_tasks())
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

