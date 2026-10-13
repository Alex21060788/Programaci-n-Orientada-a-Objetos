# Clase que representa un automóvil en el sistema.
class Car:
    """Clase que representa un automóvil en el sistema."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, brand: str, model: str, color: str) -> None:
        """Inicializa un nuevo objeto de la clase Car."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        self.brand = brand
        self.model = model
        self.color = color

    # Ahora el método show_info() está correctamente indentado dentro de la clase.
    def show_info(self) -> None:
        """Imprime en consola la información formateada del automóvil."""
        """Se usa -> None para indicar que este método no devuelve ningún valor. """

        # Agregamos la lógica para que el método realmente haga algo:
        print(f"Automóvil -> Marca: {self.brand} | Modelo: {self.model} | Color: {self.color}.\n")


# Bloque de ejecución principal.
if __name__ == "__main__":
    # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.

    # Creación del primer objeto (instancia).
    car1 = Car("Chevrolet", "Impala", "Negro")

    # Creación del segundo objeto (instancia).
    car2 = Car("Dodge", "Challenger", "Rojo")

    # Llamada al método de la clase para cada objeto.
    car1.show_info()
    car2.show_info()
