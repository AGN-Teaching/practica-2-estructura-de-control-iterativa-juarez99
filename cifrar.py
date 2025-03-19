# Plantilla cifrar.py
# cifrado.py
import random  # Importamos librería random para generar números aleatorios

def cifrar_mensaje(mensaje):
    """
    Función para cifrar un mensaje usando un desplazamiento aleatorio en el cifrado César.
    """
    k = random.randint(3, 15)  # Generamos un número aleatorio entre 3 y 15 para el desplazamiento
    mensaje_cifrado = ""  # Inicializamos la variable para almacenar el mensaje cifrado

    # Definimos los alfabetos en mayúsculas y minúsculas
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"

    # Iteramos sobre cada carácter del mensaje
    for char in mensaje:
        if char.isupper():  # Si es una letra mayúscula
            index = alfabeto_mayusculas.index(char)  # Obtenemos su índice en el alfabeto
            mensaje_cifrado += alfabeto_mayusculas[(index + k) % 26]  # Aplicamos el desplazamiento
        elif char.islower():  # Si es una letra minúscula
            index = alfabeto_minusculas.index(char)  # Obtenemos su índice en el alfabeto
            mensaje_cifrado += alfabeto_minusculas[(index + k) % 26]  # Aplicamos el desplazamiento
        else:
            mensaje_cifrado += char  # Si no es una letra, la dejamos igual

    # Añadimos el valor de k al final del mensaje cifrado para poder descifrarlo después
    mensaje_cifrado += f" {k}"

    return mensaje_cifrado, k  # Retornamos el mensaje cifrado y el valor de k

# Ejecución del programa
if __name__ == "__main__":
    mensaje = input("Introduce el mensaje a cifrar: ")  # Pedimos al usuario un mensaje
    mensaje_cifrado, k = cifrar_mensaje(mensaje)  # Ciframos el mensaje y obtenemos k
    print("Mensaje cifrado:", mensaje_cifrado)  # Mostramos el resultado cifrado
