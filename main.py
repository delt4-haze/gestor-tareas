from src.task_logic import TaskManager
from src.storage import Storage
from src.interface import show_menu, get_task_details
from src.colors import Colors

def main():
    manager = TaskManager()
    storage = Storage()
    
    while True:
        try:
            choice = show_menu()
            if choice == "1":
                title, desc = get_task_details()
                manager.add_task(title, desc)
            elif choice == "2":
                print(manager.list_tasks())
            elif choice == "3":
                print(f"{Colors.WARNING}Ayuda: Usa los números para navegar.{Colors.ENDC}")
            elif choice == "4":
                storage.save_tasks(manager.get_all_tasks())
                print(f"{Colors.GREEN}¡Hasta luego!{Colors.ENDC}")
                break
            else:
                print(f"{Colors.FAIL}Opción no válida.{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}Error: {e}{Colors.ENDC}")

# ESTA ES LA PUERTA DE ENTRADA, ¡NO PUEDE FALTAR!
if __name__ == "__main__":
    main()

