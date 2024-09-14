from autenticacion import menu_autenticacion
from gestion_cursos import menu_cursos
from gestion_usuarios import menu_usuarios
from evaluaciones import menu_evaluaciones
from progreso_estudiante import menu_progreso

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Autenticación")
        print("2. Gestión de Cursos")
        print("3. Gestión de Usuarios")
        print("4. Evaluaciones")
        print("5. Progreso del Estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_autenticacion()
        elif opcion == "2":
            menu_cursos()
        elif opcion == "3":
            menu_usuarios()
        elif opcion == "4":
            menu_evaluaciones()
        elif opcion == "5":
            menu_progreso()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_principal()
