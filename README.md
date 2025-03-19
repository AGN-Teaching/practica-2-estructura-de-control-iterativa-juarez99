# Práctica 2. Estructura de control iterativa
Informe sobre el Cifrado de Mensajes con Cifrado César
1. Presentación del Problema
El problema que se resuelve con este código es la necesidad de cifrar un mensaje de texto usando el Cifrado César, un tipo de cifrado clásico en el cual cada letra del mensaje es desplazada por un número fijo de posiciones en el alfabeto. En este caso, se utiliza un desplazamiento aleatorio entre 3 y 15 para cifrar el mensaje de forma más segura que un cifrado con un desplazamiento fijo. Este enfoque también permite la posibilidad de descifrar el mensaje al conocer el valor del desplazamiento.

El objetivo es crear una función que tome un mensaje como entrada, lo cifre aplicando el Cifrado César con un desplazamiento aleatorio, y devuelva el mensaje cifrado junto con el valor utilizado para el desplazamiento (para que pueda ser descifrado posteriormente).

2. Comentarios sobre el Diseño del Algoritmo
El diseño del algoritmo sigue una estructura sencilla y eficiente para implementar el Cifrado César con desplazamiento aleatorio. Los pasos clave del diseño son:

Generación de desplazamiento aleatorio: Utilizamos la función random.randint(3, 15) para generar un número aleatorio entre 3 y 15, lo que añade un nivel de seguridad al cifrado al hacer que el desplazamiento varíe con cada ejecución.

Recorrido del mensaje: El algoritmo recorre cada carácter del mensaje original. Dependiendo de si el carácter es una letra mayúscula, minúscula o un símbolo, se realiza un procesamiento diferente. Si es una letra, se encuentra su posición en el alfabeto correspondiente (mayúsculas o minúsculas) y se aplica el desplazamiento.

Manejo de caracteres no alfabéticos: Para los caracteres que no son letras (como espacios, signos de puntuación o números), el algoritmo los deja sin cambios. Esto mantiene la legibilidad del mensaje cifrado, permitiendo que sólo las letras sean afectadas por el desplazamiento.

Añadir el valor de desplazamiento: Al final del mensaje cifrado, se añade el valor k, que es el desplazamiento utilizado. Esto permite que el mensaje pueda ser descifrado correctamente cuando se conozca este valor.

3. Comentarios sobre la Implementación del Algoritmo en Python
La implementación del algoritmo en Python es bastante directa y clara, aprovechando las capacidades del lenguaje para manejar cadenas de texto y números aleatorios de manera eficiente. A continuación, se comentan algunos puntos clave sobre la implementación:

Uso de random.randint(): La librería random se utiliza para generar un desplazamiento aleatorio, lo cual añade un nivel de seguridad adicional al algoritmo. Al generar este valor en cada ejecución del programa, el cifrado de cada mensaje será único, lo que hace más difícil predecir o descifrar el mensaje sin conocer el desplazamiento.

Manejo de cadenas de texto: La manipulación de las cadenas de texto es simple y directa. Se utiliza un ciclo for para recorrer cada carácter del mensaje, y dependiendo de si es mayúscula, minúscula o no alfabético, se aplica el cifrado adecuado.

Alfabeto de letras: El alfabeto de letras en mayúsculas y minúsculas se define como cadenas de texto, lo que facilita la obtención del índice de cada letra y la aplicación del desplazamiento. Además, se utiliza el operador módulo % para garantizar que, al aplicar el desplazamiento, las letras "vuelvan a empezar" cuando se alcanzan las últimas posiciones del alfabeto (por ejemplo, al desplazar una "Z" o una "z").

Salida del mensaje cifrado: El mensaje cifrado se construye y luego se imprime en la consola. Al final del mensaje cifrado, se incluye el valor del desplazamiento k para que el usuario pueda descifrar el mensaje en el futuro.

4. Posibles Mejoras y Consideraciones
Seguridad: Aunque el cifrado César es adecuado para ilustrar los principios de la criptografía, no es lo suficientemente seguro para usos serios. El valor de k está incluido en el mensaje cifrado, lo que facilita el desciframiento. Una mejora sería ocultar el valor k o usar un método más seguro, como una clave secreta que no sea revelada en el mensaje cifrado.

Manejo de caracteres especiales: Si se desea cifrar textos que incluyan caracteres no alfabéticos de forma más compleja, se podría modificar el algoritmo para aplicar el desplazamiento a números o símbolos, o incluso crear un alfabeto extendido que incluya más caracteres.

Descifrado: Aunque este código implementa el cifrado, no se proporciona una función para descifrar el mensaje. Sería útil implementar un sistema de descifrado que utilice el valor k para revertir el proceso de cifrado.

Conclusión
Este código proporciona una implementación sencilla pero efectiva del Cifrado César con un desplazamiento aleatorio. Es un buen ejemplo de cómo utilizar funciones y estructuras de control de flujo en Python para aplicar un algoritmo criptográfico clásico. Aunque existen limitaciones en términos de seguridad, el enfoque es adecuado para fines educativos y de aprendizaje sobre criptografía básica.

