# Custom Exception
class AgeTooSmallError(Exception):
    """Exception raised when the input age is below the allowed threshold."""
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}."
        super().__init__(message)

class AgeTooLargeError(Exception):
    """Exception raised when the input age is above the allowed threshold."""
    def __init__(self, age, threshold=120):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is above the allowed threshold of {threshold}."
        super().__init__(message)

def check_age(age):
    """Checks if the age meets the minimum and maximum requirements."""
    if age < 18:
        raise AgeTooSmallError(age)
    elif age > 120:
        raise AgeTooLargeError(age)
    print("Acces granted")

# Example usage
try:
    age = int(input("Enter your age: "))
    check_age(age)
except AgeTooSmallError as err:
    print(f"Custom exception caught: {err}")
except AgeTooLargeError as err:
    print(f"Custom exception caught: {err}")
except ValueError:
    print("Invalid input: Please enter a valid integer.")
finally:
    print("Code processing finished!")
