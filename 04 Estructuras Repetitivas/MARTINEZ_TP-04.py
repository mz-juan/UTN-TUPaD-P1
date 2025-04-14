# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


for i in range(101):
    print(i)



#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un numero entero: "))
digitos = len(str(abs((num))))

print(f"La cantidad de digitos que contiene {num} es de: {digitos}")



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))

contador = 0
suma = 0
for contador in range (num1,num2):
    suma += contador

print(f"La suma de los numeros entre {num1} y {num2} es de: {suma}")



#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
num = int(input("Ingrese un numero: "))
suma = 0

while num != 0:
    suma = suma + num
    num = int(input("Ingrese un numero: "))

print(f"La suma total es de: {suma}")



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import * #importamos la liberioa random para generar numeros aleatorios
num_aleatorio = randint(0,10)
sumatoria = 0

num = int(input("Ingrese un numero para adivinar: "))

while num != num_aleatorio:
    print("Es incorrecto, vuelve a intentarlo")
    sumatoria += 1
    num = int(input("Ingrese un numero para adivinar: "))

print(f"Adivinaste el numero correcto {num_aleatorio} y la cantidad de intentos fueron de {sumatoria}")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

num = 0
for num in range (100,0,-2):
    print (num)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero positivo: "))
inicio = 0

contador = 0
suma = 0
for contador in range (inicio,num):
    suma += contador

print(f"La suma de los numeros entre {inicio} y {num} es de: {suma}")



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
negativos = 0
positivos = 0

for x in range (100):
    num = int(input("Ingrese un numero entero: "))
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

    if num % 2==0:
        pares += 1
    else:
        impares += 1
print(f"La cantidad de numeros positivos es de: {positivos}")
print(f"La cantidad de numeros negativos es de: {negativos}")
print(f"La cantidad de numeros pares es de: {pares}")
print(f"La cantidad de numeros impares es de: {impares}")



#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

contador = 10
suma = 0
for x in range (contador):
    num = int(input("Ingrese un numero entero: "))
    suma += num
media = suma/contador
print(f"La media de los numeros ingresados es de: {media}")



#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero: "))
num_abs = abs(num) #para impedir que el signo - se mescle con los digitos
invertir = 0

while num_abs > 0:
    digitos = num_abs % 10
    invertir = invertir *10 + digitos
    num_abs = num_abs // 10
if num < 0:
    invertir = -invertir

print(f"El numero ingresado {num} invertido es: {invertir}")