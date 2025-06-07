#1) Crea una función recursiva que calcule el factorial de un número. Luego, 
# utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

#funciones
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#main
n = int(input("Introduce un número entero: "))
print(factorial(n))

if n < 1:
    print("Ingrese un número entero positivo mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {n}:")
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")




#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

#funciones
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#main
n = int(input("Ingrese un número: "))
if n < 0:
    print("ERROR. Ingrese un número entero positivo mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {n}:")
    for i in range(n + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")





#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛^𝑚= 𝑛∗𝑛^(𝑚−1). Prueba esta función en un algoritmo general.

#funciones
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

#main
base = int(input("Ingrese la base: ")) 
exponente = int(input("Ingrese el exponente: "))
if exponente < 0:
    print("ERROR. El exponente debe ser un número entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")





#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

#funciones
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
#main
n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("ERROR. Ingrese un número entero positivo.")
else:
    resultado = decimal_a_binario(n)
    if resultado == "":
        resultado = "0"
    print(f"La representación en binario de {n} es: {resultado}")





#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

#funciones
def es_palindromo(palabra):
    #si la palabra tiene 0 o 1 caracteres, es palíndromo
    if len(palabra) <= 1:
        return True
    #compara el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    #Llama recursivamente a la función con la subcadena sin los extremos
    return es_palindromo(palabra[1:-1])

#main
palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
if es_palindromo(palabra):
    print(f"La palabra {palabra} es un palíndromo.")
else:
    print(f"La palabra {palabra} no es un palíndromo.")





#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.

#funciones
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
#main
n = int(input("Ingrese un número entero positivo: "))

if n < 0:
    print("ERROR. Ingrese un número entero positivo.")
else:
    resultado = suma_digitos(n)
    print(f"La suma de los dígitos de {n} es: {resultado}")





#7) Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.

#funciones
def contar_bloques(n):
    if n <= 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

#main
n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
if n < 1:
    print("ERROR. Ingrese un número entero positivo mayor o igual a 1.")
else:
    total_bloques = contar_bloques(n)
    print(f"El total de bloques para construir la pirámide es: {total_bloques}")





#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

#funciones
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

#main
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("ERROR. Ingrese un número entero positivo.")
else:
    digito = int(input("Ingrese un dígito entre 0 y 9: "))
    if digito < 0 or digito > 9:
        print("ERROR. Ingrese un dígito entre 0 y 9.")
    else:
        resultado = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")