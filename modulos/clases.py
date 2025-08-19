import csv
from modulos.errores import LibroNoEncontrado
from modulos.colores import RED, GREEN, YELLOW, CYAN, BOLD, RESET

class Libro:
    def __init__(self, nombre, autor, publicacion, estado):
        self.nombre = nombre
        self.autor = autor
        self.publicacion = publicacion
        self.estado = estado
    
    # __str__ siempre devuelve una cadena que representa el objeto
    def __str__(self):
        return f"{self.nombre}, Autor: {self.autor}, Año de publicación: {self.publicacion}, Estado: {'Disponible' if self.estado else 'No disponible'}"

class LibroElectronico (Libro):
    def __init__(self, nombre, autor, publicacion, estado, formato):
        super().__init__(nombre, autor, publicacion, estado)
        self.formato = formato
    
    def __str__(self):
        return f"{super().__str__()}, Formato: {self.formato}"
    

class Biblioteca:
    def __init__(self):
        self.libros = []
        # Esta línea permite que se carguen los libros al instanciar la biblioteca
        self.cargar_libros() 

    def cargar_libros(self):
        # Se abre el archivo
        try:
            with open('libros.csv', 'r', encoding='utf-8') as archivo:
                # se crea el reader del csv
                reader = csv.reader(archivo)
                #  iteración del reader 
                for row in reader:
                    # si es un libro, se crea utilizando la clase Libro
                    if len(row) == 4:
                        nombre, autor, publicacion, estado = row
                        libro = Libro(nombre, autor, publicacion, estado)
                        self.libros.append(libro)
                    # si tiene 5 valores, es un libro electronico
                    elif len(row) == 5:
                        nombre, autor, publicacion, estado, formato = row
                        libro = LibroElectronico(nombre, autor, publicacion, estado, formato)
                        self.libros.append(libro)
                    else:
                        print("Formato del libro no válido")
        # siempre hay que poner los errores más específicos  rimero para que sean capturados antes que los más ampmlios.
        except FileNotFoundError:
            print("El archivo 'libros.csv' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar los libros: {e}")

    def mostrar_libros(self):
        # iteración de los libros de la biblioteca, al imprimirlos se mostrará el __str__ de estos
        for libro in self.libros:
            print(libro)

    def agregar_libro(self):
        print("\n||||||||||||Agregar libro nuevo||||||||||||\n")
        try:
            nombre = input("Ingrese el nombre del libro: ").strip()
            autor = input("Ingrese el autor del libro: ").strip()
            publicacion = input("Ingrese el año de publicación del libro: ").strip()
            estado = input("Ingrese el estado del libro (disponible/no disponible): ").strip().lower()
            formato = input("Ingrese el formato del libro (deje vacío si es un libro físico): ").strip().lower()
            # si al agregar el libro se especifica un formato, se entiende que es un libro electronico, por lo que se instancia utilizando la clase LibroElectronico
            if formato:
                libro = LibroElectronico(nombre, autor, publicacion, estado, formato)
            else:
                libro = Libro(nombre, autor, publicacion, estado)
            # luego de eso, se agrega el libro al final de la lista de libros
            self.libros.append(libro)
            print(f"\n¡'{nombre}' agregado a la biblioteca exitosamente!.\n")
        except Exception as error:
            print(f"Error al agregar el libro. {error}")
        
    # agregué el argumento (o parámetro?) mensaje para que la misma función que sirve para buscar un libro, devuelva este para el resto de las funciones sin enviar el mensaje de búsqueda
    def buscar_libros(self, mensaje = True):
        try:
            nombre = input("Ingrese el nombre del libro: ").strip().lower()
            for libro in self.libros:
                if nombre in libro.nombre.lower():
                    if mensaje:
                        print(f'{libro.nombre} encontrado: {libro}')
                    return libro
            raise LibroNoEncontrado(f"El libro '{nombre}' no se encuentra en la biblioteca.")
        except LibroNoEncontrado as error:
            print(f"Error: {error}")
            return None
        except Exception as error:
            print(f"Error inesperado: {error}")
            return None
                

    def cambiar_estado(self, libro):
        libro.estado = not libro.estado

    def verificar_disponibilidad(self, libro):
        if libro.estado:
            print(f"El libro '{libro.nombre}' se encuentra {GREEN}disponible{RESET}.")
            opcion = input("¿Desea prestar este ejemplar? (s/n)").strip().lower()
            if opcion == "s":
                return True
            else:
                print("Operación cancelada.")
                return False
        else:
            print(f"El libro '{libro.nombre}' no está disponible para préstamo.")
            opcion = input("¿Desea devolver este ejemplar? (s/n)").strip().lower()
            if opcion == "s":
                return True
            else:
                print("Operación cancelada.")
                return False


    def prestar_libro(self):
        print("\n||||||||||||Préstamo y Devolución de libros||||||||||||\n")
        try:
            libro = self.buscar_libros(False)
            if libro:
                if self.verificar_disponibilidad(libro):
                    self.cambiar_estado(libro)
                    print(f"El libro '{libro.nombre}' ha sido {YELLOW}{"devuelto" if libro.estado else "prestado"}.{RESET}")
        except Exception as error:
            print(f"Error: {error}")

    # def devolver_libro(self):
    #     print("\n||||||||||||Devolución de libro||||||||||||\n")
    #     try:
    #         libro = self.buscar_libros(False)
    #         if libro:


    
    def eliminar_libro(self):
        print("\n||||||||||||Eliminar libro||||||||||||\n")
        try:
            libro = self.buscar_libros(False)
            if libro:
                self.libros.remove(libro)
                print(f"El libro '{libro.nombre}' ha sido eliminado de la biblioteca.")
        except LibroNoEncontrado as error:
            print(f"Error: {error}")
