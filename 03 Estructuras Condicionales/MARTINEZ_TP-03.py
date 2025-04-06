# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad") #en caso de que sea menor de 18 años


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Ingrese una nota: "))

if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. 
numero = int(input("Ingrese un numero para evaluar si es par o impar: "))

if numero % 2==0:
    print("Es un numero par")
else:
    print("Es un numero impar")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoria Adolecente")
elif edad >= 18 and edad < 30:
    print("Pertenece a la categoria Adulto/a joven")
else:
    print("Pertenece a la categoria Adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contrasenia = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if len(contrasenia) >= 8 and len(contrasenia)<= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# escribir un programa que tome la lista numeros_aleatorios,
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
# Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Lista:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif round(media, 2) == round(mediana, 2) == round(moda, 2):
    print("Sin sesgo.")
else:
    print("No hay un sesgo claro.")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
palabra = input("Ingrese una frase o palabra: ")

if palabra[-1] in "aeiouAEIOU":
    print(f"{palabra}!")
else:
    print(palabra)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese 1 si quiere su nombre en mayusculas. Ingrese 2 si quiere su nombre en minusculas. Ingrese 3 si quiere su nombre con la primera letra mayusculas: "))
mayuscula = nombre.upper()
minuscula = nombre.lower()
letra_mayus = nombre.title()


if num == 1:
    print(mayuscula)
elif num == 2:
    print(minuscula)
elif num == 3:
    print(letra_mayus)


# 9)
magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud <5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud<7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud>=7:
    print("Extremo (puede causar graves daños a gran escala).")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Ingrese en que hemisferio se encuentra (norte/sur): ")
mes = int(input("Ingrese el mes (en numeros): "))
dia = int(input("Ingrese el dia (en numeros): "))

if hemisferio == "norte":
    if (mes ==12 or mes <=3) and (dia>=21 or dia <=20):
        print("Invierno")
    elif (mes>=3 or mes <=6) and (dia>=21 or dia <=20):
        print("Primavera")
    elif (mes>=6 or mes <=9) and (dia>=21 or dia <=20):
        print("Verano")
    elif (mes>=9 or mes <=12) and (dia>=21 or dia <=20):
        print("Otoño")
elif hemisferio == "sur":
    if (mes ==12 or mes <=3) and (dia>=21 or dia <=20):
        print("Verano")
    elif (mes>=3 or mes <=6) and (dia>=21 or dia <=20):
        print("Otoño")
    elif (mes>=6 or mes <=9) and (dia>=21 or dia <=20):
        print("Invierno")
    elif (mes>=9 or mes <=12) and (dia>=21 or dia <=20):
        print("Primavera")