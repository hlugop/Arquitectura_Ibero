Software Educativo de Microservicios

Este proyecto es un sistema educativo basado en microservicios, diseñado para gestionar cursos, usuarios, evaluaciones y progreso de estudiantes de manera modular y escalable.

Descripción

El software está compuesto por varios módulos independientes que trabajan juntos para proporcionar una plataforma educativa completa:

1. **Autenticación**: Maneja el registro e inicio de sesión de usuarios.
2. **Gestión de Cursos**: Permite crear y listar cursos disponibles.
3. **Gestión de Usuarios**: Administra la creación y listado de usuarios (estudiantes y profesores).
4. **Evaluaciones**: Gestiona la creación y listado de evaluaciones para los cursos.
5. **Progreso del Estudiante**: Realiza un seguimiento y muestra el progreso de los estudiantes en los cursos.

Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- `main.py`: Punto de entrada principal que integra todos los módulos.
- `autenticacion.py`: Maneja la autenticación de usuarios.
- `gestion_cursos.py`: Gestiona la creación y listado de cursos.
- `gestion_usuarios.py`: Administra los usuarios del sistema.
- `evaluaciones.py`: Gestiona las evaluaciones de los cursos.
- `progreso_estudiante.py`: Realiza el seguimiento del progreso de los estudiantes.

Características

- Arquitectura de microservicios para mejor escalabilidad y mantenimiento.
- Interfaz de línea de comandos para fácil interacción.
- Gestión independiente de cursos, usuarios, evaluaciones y progreso.
- Sistema de autenticación básico para seguridad.

Uso

Para ejecutar el programa, navega al directorio del proyecto y ejecuta:

```
python main.py
```

Sigue las instrucciones en pantalla para navegar por los diferentes menús y funcionalidades.

Desarrollo Futuro

Este proyecto es un prototipo básico y puede ser expandido con las siguientes mejoras:

- Implementación de una base de datos para almacenamiento persistente.
- Desarrollo de una interfaz gráfica de usuario.
- Integración de un sistema de autenticación más robusto.
- Implementación de API REST para cada microservicio.
- Despliegue de cada microservicio en contenedores independientes.
