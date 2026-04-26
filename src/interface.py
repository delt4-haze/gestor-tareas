from src.colors import Colors

def show_menu():
    print(f"\n{Colors.HEADER}{Colors.BOLD}--- GESTOR DE TAREAS PRO ---{Colors.ENDC}")
    print(f"{Colors.BLUE}1.{Colors.ENDC} Agregar Tarea")
    print(f"{Colors.BLUE}2.{Colors.ENDC} Listar Tareas")
    print(f"{Colors.BLUE}3.{Colors.ENDC} Ayuda")
    print(f"{Colors.FAIL}4.{Colors.ENDC} Guardar y Salir")
    return input(f"{Colors.BOLD}Selecciona una opción: {Colors.ENDC}")

def get_task_details():
    title = input("Título de la tarea: ")
    desc = input("Descripción: ")
    return title, desc

