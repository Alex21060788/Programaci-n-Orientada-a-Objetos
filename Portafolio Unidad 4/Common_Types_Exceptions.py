def probar_excepciones(opcion):
    try:
        if opcion == 1:
            # 1. ValueError: tipo correcto (str), pero valor inapropiado
            numero = int("abc")

        elif opcion == 2:
            # 2. TypeError: operación entre tipos incompatibles
            resultado = "texto" + 5

        elif opcion == 3:
            # 3. ZeroDivisionError: división entre cero
            division = 10 / 0

        elif opcion == 4:
            # 4. IndexError: índice fuera del rango de la lista
            lista = [1, 2, 3]
            elemento = lista[10]

        elif opcion == 5:
            # 5. KeyError: clave inexistente en el diccionario
            diccionario = {"nombre": "Ana"}
            valor = diccionario["edad"]

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

# Ejecutamos cada caso para ver cómo se captura cada excepción
opcion = int(input("Elige un error para probar (1 al 5): "))
probar_excepciones(opcion)
