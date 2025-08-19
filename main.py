from modulos.clases import Libro, LibroElectronico, Biblioteca
from modulos.colores import RED, GREEN, YELLOW, CYAN, BOLD, RESET

biblioteca = Biblioteca()

def menu():
    while True:
        print(f'''{YELLOW}{BOLD}¡Bienvenido al Sistema de Gestión de libros!{RESET}\nPor favor, ingrese una opción:''')
        print(f'''{CYAN}{BOLD}1. Agregar libro{RESET}\n{CYAN}{BOLD}2. Buscar libro{RESET}\n{CYAN}{BOLD}3. Eliminar libro{RESET}\n{CYAN}{BOLD}4. Prestar libro{RESET}\n{CYAN}{BOLD}5. Mostrar todos los libros{RESET}\n{CYAN}{BOLD}6. Salir{RESET}''')
        opcion = input(f"{GREEN}Ingrese su opción: {RESET}")
        if opcion == "1":
            biblioteca.agregar_libro()
        elif opcion == "2":
            print("\n||||||||||||Búsqueda de libro||||||||||||\n")
            biblioteca.buscar_libros()
        elif opcion == "3":
            biblioteca.eliminar_libro()
        elif opcion == "4":
            biblioteca.prestar_libro()
        elif opcion == "5":
            biblioteca.mostrar_libros()
        elif opcion == "6":
            print(f"{YELLOW}¡Hasta luego!{RESET}")
            break
        else:
            print(f"{RED}Opción no válida. Por favor, intente de nuevo.{RESET}")

if __name__ == "__main__":
    menu()