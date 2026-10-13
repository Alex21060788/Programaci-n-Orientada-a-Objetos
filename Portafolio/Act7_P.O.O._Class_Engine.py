# Clase motor dentro del sistema.
class Engine:
    """Representa el motor de un vehículo dentro del sistema."""

    # Ahora el método está correctamente indentado dentro de la clase.  
    def __init__(self, horsepower: int, engine_type: str) -> None:
        """Inicializa una nueva instancia de la clase Engine."""
        """"El formato : int e : str son pista de tipo (type hint) que indican que se esperan enteros y textos (ints y strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        self.horsepower = horsepower
        self.engine_type = engine_type

    # Ahora el método está correctamente indentado dentro de la clase   
    def start(self) -> str:
        """Simula el arranque del motor y genera el mensaje de estado."""
        """Se usa -> str para indicar que retorna un valor en cadena (Mensaje indicando que el motor ha arrancado)."""

        return f"The {self.engine_type} engine with {self.horsepower} HP is starting."

# Clase carro dentro del sistema.
class Car:
    """Representa un automóvil que posee un motor (Composición)."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, brand: str, engine: Engine) -> None:
        """Inicializa una nueva instancia de la clase Car."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """El formato : Engine es una pista de tipo (type hint) que indica que una variable, argumento o retorno de función debe ser una instancia de una clase llamada Engine."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""
        
        self.brand = brand
        self.engine = engine  # Guardamos el objeto motor completo aquí

    def start_car(self) -> None:
        """Enciende el automóvil activando primero su motor."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""
        
        print(f"Starting the {self.brand} car...")

        # Accedemos al método start() del objeto motor que está guardado dentro de este coche.
        print(self.engine.start())


# Bloque de ejecución principal
if __name__ == "__main__":
    print("--- Configurando los Componentes del Auto ---")
    
    # Creamos primero el motor con los tipos de datos correctos (int, str)
    my_engine = Engine(horsepower=350, engine_type="V8")
    
    # Creamos el coche y le "inyectamos" el motor que acabamos de fabricar
    my_car = Car(brand="Ford Mustang", engine=my_engine)
    
    print("\n--- Probando el Funcionamiento del Coche ---")
    
    # Arrancamos el coche, lo cual a su vez encenderá su propio motor interno
    my_car.start_car()
