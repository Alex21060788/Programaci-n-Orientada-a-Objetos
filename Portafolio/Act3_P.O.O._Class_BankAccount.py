# Clase que representa una cuenta bancaria e incluye operaciones monetarias básicas.
class BankAccount:
    """Clase que representa una cuenta bancaria e incluye operaciones monetarias básicas."""

    # Ahora el método está correctamente indentado dentro de la clase.
    def __init__(self, bank_name: str, account_holder: str, balance: float) -> None:
        """Inicializa una nueva instancia de BankAccount."""
        """El formato : str es una pista de tipo (type hint) que indica que se esperan textos (strings)."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        self.bank_name = bank_name
        self.account_holder = account_holder
        self.balance = balance

    # Ahora el método show_balance() está correctamente indentado dentro de la clase.
    def show_balance(self) -> None:
        """Imprime en consola el titular y el saldo actual de la cuenta."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}.\n")

    # Ahora el método show_bank() está correctamente indentado dentro de la clase.
    def show_bank(self) -> None:
        """Imprime en consola el nombre de la institución bancaria."""
        """Se usa -> None para indicar que este método no devuelve ningún valor."""

        print(f"Bank name: {self.bank_name}.\n")

    # Ahora el método convert_currency() está correctamente indentado dentro de la clase.
    @staticmethod
    def convert_currency(value: float) -> float:
        """Convierte un valor numérico de dólares (USD) a pesos mexicanos (MXN)."""
        """El formato : float es una pista de tipo (type hint) que indica que se esperan flotantes (flotantes)."""
        """Se usa -> float: para indicar que retorna un valor flotante (El monto equivalente en pesos)."""

        conversion_rate = 17.79
        return value * conversion_rate
 

#  Bloque de ejecución principal.
if __name__ == "__main__":
    # Los comentarios descriptivos de procesos los debo escribir con '#' y no con docstrings.

    # Instanciación de la cuenta bancaria.
    account1 = BankAccount(bank_name="Central Bank", account_holder="Joe Keery", balance=1000.0)

    # Inspección de atributos del objeto.
    print("--- Datos de la cuenta ---")
    print(f"Bank: {account1.bank_name}, Holder: {account1.account_holder}, Balance: ${account1.balance:.2f}.\n")

    # Uso de los métodos de instancia.
    print("--- Métodos de Instancia ---")
    account1.show_bank()
    account1.show_balance()

    # Uso del método estático (invocado desde la clase y capturando su retorno).
    print("\n--- Método Estático ---")
    usd_amount = 500.0
    mxn_equivalent = BankAccount.convert_currency(usd_amount)
    print(f"${usd_amount:.2f} USD equivalen a ${mxn_equivalent:.2f} MXN.\n")
