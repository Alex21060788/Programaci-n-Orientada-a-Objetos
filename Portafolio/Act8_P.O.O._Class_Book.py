class Book:
    def __init__(self, title: str, num_pages: int):
        """Inicializa una instancia libro con su titulo y numero de paginas."""

        self.title = title
        self.num_pages = num_pages

    def __str__(self) -> str:
        """Sobrescribe la representación de cadena para la impresión "Book: X, Pages: Y."""

        return f"Book: {self.title}, Pages: {self.num_pages}"

    def __len__(self) -> int:
        """Sobrescribe len() para que len(book) devuelva el número de páginas."""

        return self.num_pages


# Bloque de ejecución principal.
if __name__ == "__main__":
   # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.

    # Crea una instancia de la clase Book.
    my_book = Book("Hábitos Atómicos", 328)

    # Prueba la redefinición de __str__() (invocada automáticamente por print())
    print(my_book)  

    # Resultado: Libro: Hábitos Atómicos, Páginas: 328

    # Prueba la redefinición de __len__() (que se activa al llamar a len())
    pages_count = len(my_book)
    print(f"The book has {pages_count} pages.")  
    # Resultadd: El libro tiene 328 paginas.
