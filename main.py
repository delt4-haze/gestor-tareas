from logica import cargar_tareas, guardar_tareas

def main():
    tareas = cargar_tareas()
    while True:
        print("\n--- GESTOR DE TAREAS (GitHub Ready) ---")
        print("1. Ver tareas | 2. Añadir | 3. Salir")
        opc = input("Selecciona: ")
        
        if opc == '1':
            for i, t in enumerate(tareas):
                print(f"{i+1}. {t}")
        elif opc == '2':
            nueva = input("Tarea: ")
            tareas.append(nueva)
            guardar_tareas(tareas)
            print("Guardado.")
        elif opc == '3':
            break

if __name__ == "__main__":
    main()
