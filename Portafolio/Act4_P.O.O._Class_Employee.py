# Clase que representa a un empleado dentro del sistema.
class Employee:
    """Clase que representa a un empleado dentro del sistema."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, name: str, salary: float) -> None:
        """Inicializa un nuevo objeto de la clase Employee."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""
        
        self.name = name
        self.salary = salary

    # Ahora el método show_info() está correctamente indentado dentro de la clase.
    def show_info(self) -> None:
        """Muestra en consola la información básica del empleado."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Name: {self.name}, Salary: {self.salary}.\n")


# Clase Manager que hereda de Employee.
class Manager(Employee):
    """Clase que representa a un gerente, heredando de la clase Employee."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, name: str, salary: float, department: str) -> None:
        """Inicializa un nuevo objeto de la clase Manager."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """"Se usa -> None para indicar que este método no devuelve ningún valor."""

        # Llamada al constructor de la clase base (Employee).
        super().__init__(name, salary)
        self.department = department

    # Ahora el método show_info() está correctamente indentado dentro de la clase.
    def show_info(self) -> None:
        """Muestra la información completa del gerente, incluyendo su departamento."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        # Llamada al método show_info de la clase base (Employee).
        super().show_info()
        print(f"Department: {self.department}.\n")


# Bloque de ejecución principal.
if __name__ == "__main__":
    # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.
    
    # Objeto 1: Instancia de la clase base.
    employee1 = Employee("Sam Winchester", 30000.0)
    print("--- Información del Empleado ---")
    employee1.show_info()
          
    # Objeto 2: Instancia de la clase heredada (Hijo).
    manager1 = Manager("Dean Winchester", 50000.0, "Sales")
    print("--- Información del Gerente ---")
    manager1.show_info()
