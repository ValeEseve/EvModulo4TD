# Sistema de Gestión de Biblioteca

Utilizando un archivo csv como base, construí este programa que sirve para gestionar una pequeña biblioteca.

Construí la base de datos de libros incluyendo nombre, autor, año de publicación, disponibilidad y formato (en el caso de los libros electrónicos).

Teniendo esto en cuenta, creé las clases Libro y LibroElectronico. El segundo hereda los atributos del primero y añade formato tanto a su valor de __str__ como a sus atributos.

Respecto a lo anterior, implementé el método especial __str__ para definir una representación legible de estas clases. Debido a esto, cuando se "imprima" cada objeto, lo que se verá en la consola será el código escrito en esa línea.

Al iniciar el programa, se instancia la clase Biblioteca. Es en ese momento que se realiza la carga de los libros en la memoria temporal del programa a través de la función cargar_libros, que abre el archivo CSV, lo recorre línea por línea y crea los objetos correspondientes según si se trata de un libro físico o electrónico.

#### Funcionalidades principales

##### Mostrar libros:
Se recorre la lista de libros de la biblioteca y se imprime cada uno en pantalla, utilizando su método __str__. Esto permite visualizar la información de manera clara y legible.

##### Guardar libros
Cada vez que se hacen cambios en los libros de la biblioteca, se actualiza el csv, al ser llamada tanto al agregar o eliminar libros.

##### Agregar libros:
Se solicita al usuario ingresar los datos básicos del libro (nombre, autor, año, estado y, opcionalmente, formato).

Si se indica un formato, se instancia un objeto de la clase LibroElectronico.

Si no se indica formato, se instancia un objeto de la clase Libro.
El nuevo libro se agrega a la lista de libros en memoria.

##### Eliminar libros:
Permite buscar un libro y, en caso de existir, eliminarlo de la lista de la biblioteca. Si no se encuentra, se captura la excepción correspondiente y se muestra el mensaje de error.

##### Buscar libros:
Se implementó un método que permite buscar un libro por su nombre (o parte de él). Si el libro existe, se retorna el objeto correspondiente; si no, se lanza una excepción personalizada (LibroNoEncontrado).
Este método además puede funcionar silenciosamente (sin imprimir mensajes) para ser reutilizado en otras funciones internas de la biblioteca.

##### Préstamo y devolución de libros:
Se selecciona un libro mediante la búsqueda y se consulta al usuario si desea prestar o devolver el ejemplar según su estado actual.
Para esto, se utilizan los métodos:

verificar_disponibilidad: muestra el estado del libro y pide confirmación.

cambiar_estado: alterna entre disponible y no disponible según la acción realizada.


#### Manejo de errores

El código incluye un control de errores en distintos niveles:

Durante la carga inicial de libros desde el archivo CSV (por ejemplo, si el archivo no existe).

En la búsqueda de libros mediante la excepción personalizada LibroNoEncontrado.

En las funciones que interactúan con el usuario, manejando entradas inesperadas para evitar que el programa se detenga abruptamente.

#### Uso de colores

Con el objetivo de hacer más amigable la interacción en consola, se integró un módulo externo que define códigos de color para resaltar información importante, como disponibilidad de libros o resultados de operaciones.