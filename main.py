from modulos.clases import Libro, LibroElectronico, Biblioteca




biblioteca = Biblioteca()
biblioteca.buscar_libros()
biblioteca.eliminar_libro()

def menu():
    while True:
        print('''¡Bienvenido al Sistema de Gestión de libros!
          Por favor, ingrese una opción:''')

if __name__ == "__main__":
    menu()