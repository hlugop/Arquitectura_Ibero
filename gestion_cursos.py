cursos = {}

def crear_curso(nombre, descripcion):
    if nombre in cursos:
        return "El curso ya existe"
    cursos[nombre] = descripcion
    return "Curso creado exitosamente"

def listar_cursos():
    return "\n".join([f"{nombre}: {descripcion}" for nombre, descripcion in cursos.items()])

def menu_cursos():
    while True:
        print("\n--- Menú de Gestión de Cursos ---")
        print("1. Crear curso")
        print("2. Listar cursos")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre del curso: ")
            descripcion = input("Ingrese descripción del curso: ")
            print(crear_curso(nombre, descripcion))
        elif opcion == "2":
            print(listar_cursos())
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
