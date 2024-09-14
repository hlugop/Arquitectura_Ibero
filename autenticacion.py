def menu_autenticacion():
    print("=== Menú de Autenticación ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    
    while True:
        opcion = input("Seleccione una opción (1-3): ")
        if opcion in ['1', '2', '3']:
            return opcion
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Función para iniciar sesión
def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    # Aquí iría la lógica de verificación de credenciales
    print(f"Intento de inicio de sesión para el usuario: {usuario}")
    return False  # Por ahora, siempre retorna False

# Función para registrarse
def registrarse():
    nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ")
    nueva_contraseña = input("Ingrese una nueva contraseña: ")
    # Aquí iría la lógica para guardar el nuevo usuario
    print(f"Nuevo usuario registrado: {nuevo_usuario}")
    return True

# Función principal de autenticación
def autenticar():
    while True:
        opcion = menu_autenticacion()
        if opcion == '1':
            if iniciar_sesion():
                print("Inicio de sesión exitoso.")
                return True
            else:
                print("Credenciales incorrectas. Intente de nuevo.")
        elif opcion == '2':
            if registrarse():
                print("Registro exitoso. Por favor, inicie sesión.")
            else:
                print("Error en el registro. Intente de nuevo.")
        elif opcion == '3':
            print("Saliendo del sistema de autenticación.")
            return False

# Asegúrate de que estas funciones estén disponibles para importar
