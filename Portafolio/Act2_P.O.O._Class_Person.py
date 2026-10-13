# Clase que representa a una persona dentro del sistema.
class Person:
    """Clase que representa a una persona dentro del sistema."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, name: str, age: int, city: str) -> None:
        """Inicializa un nuevo objeto de la clase Person."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""
        
        self.name = name
        self.age = age
        self.city = city

    # Ahora el método greet() está correctamente indentado dentro de la clase.
    def greet(self) -> None:
        """Imprime un saludo con la información detallada de la persona."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.\n")


# Bloque de ejecución principal.
if __name__ == "__main__":
    # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.

    # Creación de los objetos (instancias).
    person1 = Person("Donovan", 19, "Tepic")
    person2 = Person("Bryan", 19, "Tepic")
    person3 = Person("Javier", 19, "Tepic")

    # Llamada al método greet() para que el objeto genere el saludo.
    person1.greet()
    person2.greet()
    person3.greet()
