#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#Funciones
def imprimir_hola_mundo():
    return print("hola mundo!")

#Programa principal
imprimir_hola_mundo()




#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
#“Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#funciones
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)




#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
#los datos al usuario y llamar a esta función con los valores ingresados.

#Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)




#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados.

#Funciones
def calcular_area_circulo(radio):
    area = 3.14*(radio)**2
    return area
def calcular_perimetro_circulo(radio):
    Perimetro = 2*3.14*radio
    return Perimetro

#Programa principal
radio = float(input("Ingrese el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f" el area es de {area}  el perimetro es {perimetro}")




#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar
#el resultado usando esta función.

#Funciones
def segundos_a_horas(segundos):
    return print(f"En horas son: {segundos/3600}")

#Programa principal
segundos = segundos_a_horas(int(input("Ingrese los segundos para convertirlos a horas: ")))




#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Funciones
def tabla_multiplicar(numero):
    for i in range (1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
    return 

#Programa principal
numero = tabla_multiplicar(int(input("Ingrese un numero: ")))




#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
#de forma clara.

#Funciones
def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    if b != 0:
        division = a/b
    else:
        print("No se puede dividir por cero")
    return (suma, resta, multiplicacion, division) #tupla o lista de numeros [0, 1, 2, 3]

#Programa principal
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))
resulados = operaciones_basicas(num1, num2)

print(f"EL resultado de sumarlos es: {resulados[0]}")
print(f"EL resultado de restarlos es: {resulados[1]}")
print(f"EL resultado de multiplicarlos es: {resulados[2]}")
print(f"EL resultado de dividirlos es: {resulados[3]}")




#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales.

#Funciones
def calcular_imc(peso, altura):
    resultado = peso/(altura)**2
    return round(resultado, 2)

#Programa principal
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
resultado = calcular_imc(peso, altura)

print(f"Su indice de masa corporal (imc) es de: {resultado}")




#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#Funciones
def celsius_a_fahrenheit(celsius):
    resultado = (celsius*1.8)+32
    return resultado

#Programa Principal
celsius = float(input("Ingrese una temperatura en grados celsius: "))
resultado = celsius_a_fahrenheit(celsius)

print(f"La conversion de {celsius} grados celsius a fahrenheit es: {resultado}")




#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

#Funciones
def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma/3
    return promedio

#Programa Principal
num1 = float(input("Ingrese la primer nota: "))
num2 = float(input("Ingrese la segunda nota: "))
num3 = float(input("Ingrese la tercer nota: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio entre {num1}, {num2} y {num3} es de: {promedio}")