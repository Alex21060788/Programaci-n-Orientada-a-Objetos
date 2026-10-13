# Clase que representa a un contador en el sistema.
class Accountant:
    """Clase que representa a un contador encargado de tareas financieras."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, name: str, department: str) -> None:
        """Inicializa una nueva instancia de la clase Accountant."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""
        
        self.name = name
        self.department = department

    # Ahora el método generate_report() está correctamente indentado dentro de la clase.
    def generate_report(self) -> None:
        """Genera y muestra en consola un reporte financiero básico."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Accountant {self.name} from {self.department} department is generating a financial report.\n")


# Clase que representa a un técnico en el sistema.
class Technician:
    """Clase que representa a un técnico encargado del mantenimiento."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, name: str, department: str) -> None:
        """Inicializa una nueva instancia de la clase Technician."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        self.name = name
        self.department = department

    # Ahora el método está correctamente indentando dentro de la clase.
    def repair_machine(self) -> None:
        """Simula la acción de reparar una máquina del sistema."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Technician {self.name} from {self.department} department is repairing a machine.\n")


# Boss hereda de ambas clases (Herencia Múltiple).
class Boss(Accountant, Technician):
    """Clase que representa a un jefe que combina habilidades contables y técnicas."""
    """Hereda de las clases Accountant y Technician de forma simultánea."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, name: str, department: str) -> None:
        """Inicializa una nueva instancia de Boss, coordinando sus clases base."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        # En herencia múltiple simple con atributos idénticos, super() inicializa correctamente siguiendo el MRO (Method Resolution Order).
        super().__init__(name, department)

    # Ahora el método generate_report() está correctamente indentado dentro de la clase.
    def generate_report(self) -> None:
        """Genera un reporte financiero con el rango superior de Boss."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""
        
        print(f"Boss {self.name} from {self.department} department is generating a financial report.\n")

    # Ahora el método repair_machine() está correctamente indentado dentro de la clase.
    def repair_machine(self) -> None:
        """Repara una máquina con el rango superior de Boss."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Boss {self.name} from {self.department} department is repairing a machine.\n")


# Bloque de ejecución principal.
if __name__ == "__main__":
    # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.

    # Instancia de Accountant (Contador).
    accountant1 = Accountant("Mike Ross", "Finance")
    print("--- Acción del Contador ---")
    accountant1.generate_report()

    # Instancia de Technician (Técnico).
    technician1 = Technician("Benjamin Reale", "Information Technology")
    print("--- Acción del Técnico ---")
    technician1.repair_machine()

    # Instancia de Boss llamando a sus métodos heredados y modificados.
    boss1 = Boss("Harvey Specter", "Legal")
    print("--- Acciones del Jefe (Boss) ---")
    boss1.generate_report()  