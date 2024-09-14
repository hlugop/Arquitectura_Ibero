usuarios = {}

def crear_usuario(nombre, rol):
    if nombre in usuarios:
        return "El usuario ya existe"
    usuarios[nombre] = rol
    return "Usuario creado exitosamente"

def listar_usuarios():
    return "\n".join([f"{nombre}: {rol}" for nombre, rol in usuarios.items()])

def menu_usuarios():
    while True:
        print("\n--- Menú de Gestión de Usuarios ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese nombre del usuario: ")
            rol = input("Ingrese rol del usuario (estudiante/profesor): ")
            print(crear_usuario(nombre, rol))
        elif opcion == "2":
            print(listar_usuarios())
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
