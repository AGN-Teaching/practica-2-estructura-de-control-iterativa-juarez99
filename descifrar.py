# Plantilla descifrar.py

def descifrar_mensaje(mensaje_cifrado, k):
    """
    Función para descifrar un mensaje cifrado con el Cifrado César usando el valor de desplazamiento k.
    """
    mensaje_descifrado = ""  # Inicializamos la variable para almacenar el mensaje descifrado

    # Definimos los alfabetos en mayúsculas y minúsculas
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"

    # Analizamos cada letra del mensaje
    for char in mensaje_cifrado:
        if char.isupper():  # Si es una letra mayúscula
            index = alfabeto_mayusculas.index(char)  # Obtenemos su índice en el alfabeto
            mensaje_descifrado += alfabeto_mayusculas[(index - k) % 26]  # Aplicamos el desplazamiento negativo
        elif char.islower():  # Si es una letra minúscula
            index = alfabeto_minusculas.index(char)  # Obtenemos su índice en el alfabeto
            mensaje_descifrado += alfabeto_minusculas[(index - k) % 26]  # Aplicamos el desplazamiento negativo
        else:
            mensaje_descifrado += char  # Si no es una letra, la dejamos igual

    return mensaje_descifrado  # Retornamos el mensaje descifrado


# Ejecución del programa
if __name__ == "__main__":
    mensaje_cifrado = input("Introduce el mensaje cifrado: ")  # Pedimos al usuario un mensaje cifrado
    k = int(input("Introduce el valor de desplazamiento k: "))  # Pedimos el valor de k (debe ser el mismo que se usó para cifrar)
    
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, k)  # Desciframos el mensaje
    print("Mensaje descifrado:", mensaje_descifrado)  # Mostramos el resultado descifrado
