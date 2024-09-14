evaluaciones = {}

def crear_evaluacion(nombre, curso):
    if nombre in evaluaciones:
        return "La evaluación ya existe"
    evaluaciones[nombre] = curso
    return "Evaluación creada exitosamente"

def listar_evaluaciones():
    return "\n".join([f"{nombre}: {curso}" for nombre, curso in evaluaciones.items()])

def menu_evaluaciones():
    while True:
        print("\n--- Menú de Evaluaciones ---")
        print("1. Crear evaluación")
        print("2. Listar evaluaciones")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre de la evaluación: ")
            curso = input("Ingrese curso al que pertenece: ")
            print(crear_evaluacion(nombre, curso))
        elif opcion == "2":
            print(listar_evaluaciones())
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
