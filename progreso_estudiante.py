progreso_estudiantes = {}

def actualizar_progreso(estudiante, curso, porcentaje):
    if estudiante not in progreso_estudiantes:
        progreso_estudiantes[estudiante] = {}
    progreso_estudiantes[estudiante][curso] = porcentaje
    return "Progreso actualizado exitosamente"

def obtener_progreso(estudiante):
    if estudiante not in progreso_estudiantes:
        return "Estudiante no encontrado"
    return "\n".join([f"{curso}: {porcentaje}%" for curso, porcentaje in progreso_estudiantes[estudiante].items()])

def menu_progreso():
    while True:
        print("\n--- Menú de Progreso del Estudiante ---")
        print("1. Actualizar progreso")
        print("2. Obtener progreso")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            estudiante = input("Ingrese nombre del estudiante: ")
            curso = input("Ingrese nombre del curso: ")
            porcentaje = input("Ingrese porcentaje de progreso: ")
            print(actualizar_progreso(estudiante, curso, porcentaje))
        elif opcion == "2":
            estudiante = input("Ingrese nombre del estudiante: ")
            print(obtener_progreso(estudiante))
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
