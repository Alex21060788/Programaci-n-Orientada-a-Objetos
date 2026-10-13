# Clase base para el cálculo de pagos de los empleados.
class CalculatePayment:
    """Clase base encargada de procesar el cálculo de pago de un empleado."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, salary: float, hours_worked: int) -> None:
        """Inicializa una nueva instancia de la clase CalculatePayment."""
        """Los formatos : float e : int son pista de tipo (type hint) que indican que se esperan flotantes y enteros (floats e ints)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        self.salary = salary
        self.hours_worked = hours_worked

    # Ahora el método payment() está correctamente indentado dentro de la clase.
    def payment(self) -> float:
        """Calcula el pago total multiplicando el salario por las horas."""
        """Se usa -> float: para indicar que retorna un valor flotante (El monto total acumulado del pago)."""
            
        return self.salary * self.hours_worked


# Clase FullTimeEmployee que hereda de CalculatePayment.
class FullTimeEmployee(CalculatePayment):
    """Representa a un empleado de tiempo completo."""
    """Hereda la lógica de cálculo de la clase CalculatePayment."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, salary: float, hours_worked: int) -> None:
        """Inicializa un empleado de tiempo completo usando el constructor base."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        super().__init__(salary, hours_worked)

    # Ahora el método payment() está correctamente indentado dentro de la clase.
    def payment(self) -> float:
        """Calcula el pago correspondiente para el empleado de tiempo completo."""
        """Se usa -> float para indicar que retorna un valor flotante (El pago calculado a traves de la clase base)."""
        
        return super().payment()


# Clase HourlyEmployee que hereda de CalculatePayment.
class HourlyEmployee(CalculatePayment):
    """Representa a un empleado que trabaja bajo un esquema de pago por horas."""
    """Hereda la lógica de cálculo de la clase CalculatePayment."""
    
    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, salary: float, hours_worked: int) -> None:
        """Inicializa un empleado por horas usando el constructor base."""
        """Los formatos : float e : int son pista de tipo (type hint) que indican que se esperan flotantes y enteros (floats e ints)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        super().__init__(salary, hours_worked)

    # Ahora el método payment() está correctamente indentado dentro de la clase.
    def payment(self) -> float:
        """Calcula el pago correspondiente para el empleado por horas."""
        """Se usa para -> float para indicar que retorna un valor flotante (El pago calculado a traves de la clase base)."""

        return super().payment()


# Bloque de ejecución principal.
if __name__ == "__main__":
    # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.

    # Instancias de las clases.
    payment_base = CalculatePayment(200.0, 40)
    employee_full_time = FullTimeEmployee(300.0, 40)
    employee_hourly = HourlyEmployee(15.0, 40)

    # Es necesario envolver .payment() en un print() para poder ver el return en consola.
    print("--- Resultados de los Pagos de Empleados ---")
    print(f"Pago Empleado Base:        ${payment_base.payment():.2f}.\n")
    print(f"Pago Empleado Tiempo Completo: ${employee_full_time.payment():.2f}.\n")
    print(f"Pago Empleado Por Horas:   ${employee_hourly.payment():.2f}.\n")
