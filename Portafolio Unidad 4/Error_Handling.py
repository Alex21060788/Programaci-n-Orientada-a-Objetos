"""
¿Qué hace este programa?
Pide al usuario su edad y revisa si está entre 18 y 120 años.
Si el número es muy bajo, muy alto o si escriben letras por error,
el programa atrapa el problema y muestra un mensaje claro sin cerrarse de golpe.
"""

# 1. Creamos alertas propias (ya que Python no sabe qué edades permite nuestro sistema)
class AgeTooSmallError(Exception):
    """Alerta que se activa cuando la edad ingresada es menor a 18 años."""
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}."
        super().__init__(message)


class AgeTooLargeError(Exception):
    """Alerta que se activa cuando la edad ingresada es mayor a 120 años."""
    def __init__(self, age, threshold=120):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is above the allowed threshold of {threshold}."
        super().__init__(message)


# 2. Función que revisa si el número cumple con las reglas
def check_age(age):
    """Comprueba la edad: si está fuera de rango, lanza una alerta; si no, da acceso."""
    if age < 18:
        raise AgeTooSmallError(age)   # Activa la alerta de edad muy baja
    elif age > 120:
        raise AgeTooLargeError(age)   # Activa la alerta de edad muy alta
    print("Acces granted")


# 3. Ejecución protegida (atrapa errores para evitar fallos bruscos)
try:
    age = int(input("Enter your age: "))  # Pide el dato y lo convierte a número
    check_age(age)                        # Revisa si cumple con la regla de edad

except AgeTooSmallError as err:
    # Atrapa el error si es menor de 18
    print(f"Custom exception caught: {err}")

except AgeTooLargeError as err:
    # Atrapa el error si es mayor de 120
    print(f"Custom exception caught: {err}")

except ValueError:
    # Atrapa el error si el usuario escribió letras o símbolos en vez de un número
    print("Invalid input: Please enter a valid integer.")

finally:
    # Este mensaje aparece SIEMPRE al terminar, sin importar si hubo error o no
    print("Code processing finished!")
