"""
¿Qué hace este programa?
Es un menú interactivo de práctica. Te deja elegir un número del 1 al 5
para provocar a propósito los 5 errores más comunes al programar, y muestra
cómo atraparlos con mensajes fáciles de entender.
"""

def probar_excepciones(opcion):
    """Provoca un error según el número elegido (1-5) y lo traduce a un aviso claro."""
    try:
        if opcion == 1:
            # 1. Dato mal escrito: intenta convertir letras ("abc") en un número
            numero = int("abc")

        elif opcion == 2:
            # 2. Mezcla incompatible: intenta sumar una palabra con un número
            resultado = "texto" + 5

        elif opcion == 3:
            # 3. Matemática imposible: intenta dividir entre cero
            division = 10 / 0

        elif opcion == 4:
            # 4. Posición inexistente: la lista tiene 3 datos, pero pide el número 10
            lista = [1, 2, 3]
            elemento = lista[10]

        elif opcion == 5:
            # 5. Etiqueta perdida: busca "edad" en una ficha que solo tiene "nombre"
            diccionario = {"nombre": "Ana"}
            valor = diccionario["edad"]

    # "Paracaídas" que atrapan cada error y muestran una explicación sencilla:
    except ValueError:
        print("Error (ValueError): No se puede convertir ese valor a entero.")
    except TypeError:
        print("Error (TypeError): No se pueden operar tipos de datos incompatibles.")
    except ZeroDivisionError:
        print("Error (ZeroDivisionError): No es posible dividir entre cero.")
    except IndexError:
        print("Error (IndexError): El índice está fuera del rango de la lista.")
    except KeyError:
        print("Error (KeyError): La clave buscada no existe en el diccionario.")


# Pedimos al usuario que elija qué error quiere poner a prueba
opcion = int(input("Elige un error para probar (1 al 5): "))
probar_excepciones(opcion)

