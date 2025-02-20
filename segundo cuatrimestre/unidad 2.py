#Ejercico 1
# number  = input('escribir numero entero: .....')
# print(number)

#Ejercicio 2: 
# num1 = int(input("ingresa un numero entero: "))

# num2 = int(input("ingresa otro numero entero: "))

# print(f'numeros elegidos, {num1} y el {num2}')

# suma = num1 + num2
# resta = num1 - num2
# mult  = num1 * num2
# div = num1/num2

# print(f"suma: {suma}")
# print(f"resta: {resta}")
# print(f"mult: {mult}")
# print(f"div: {div}")

#ejericio 3:
# print("programa que determina si un número es par")

# number = int(input("ingrese un numero entero: "))

# valor = number % 2

# if valor == 0:
#     print(f"el número {number} es par")
# else : print(f"el número {number} es impar")

#ejercicio 4:
# print("programa que calcula edades")
# año_de_nacimiento = input("ingrese su año de nacimiento: ")

# while año_de_nacimiento.isdigit() == False:
#     print("el año de nacimiento es una fecha positiva y entera, intente de nievo, ")
#     año_de_nacimiento = input("ingrese su año de nacimiento: ")

# año = input("ingrese otro año: ")
# while año.isdigit() == False:
#     print("el año de es una fecha positiva y entera, intente de nievo, ")
#     año_de_nacimiento = input("ingrese el año que quiere calcular su edad: ")

# edad = int(año) - int(año_de_nacimiento)
# print(f"su edad en el año {año} era de {edad} años")

#ejercicio 5:
# print("programa que calcula el promedio, para ellos vamos a necesitar 5 numeros")
# suma = 0
# for i in range(1,6):
#     if i == 1: 
#         number = input("ingresá un número: ")
#     number = input("ingresá otro número: ")
#     while number.isdigit() == False :
#         print("tenés que ingresar un número entero que sea positivo")
#         number = input("ingresá un número entero positivo: ")
#     numero = int(number)
#     suma += numero
# promedio = suma / 5
# print(f"el promedio de la suma es {promedio}")

#ejercicio 6:
# print("función que dice el anterior y el siguiente de un número")
# def calculator(number): 
#     anterior = number -1
#     siguiente = number + 1

#     return {"anterior": anterior, "siguiente": siguiente}
# number = input("ingesá un número: ")
# datos = calculator(int(number))
# ant = datos["anterior"]
# print(f"anterior: {ant}")
# sig = datos["siguiente"]
# print(f"siguiente: {sig}")

#ejercicio 7:
# def unidor(number, text): 
#     mezcla = str(number) + " " + text
#     return mezcla

# number = int(input("ingresa un numero: "))

# text = input("ingresá un texto: ")

# union = unidor(number, text)
# print(union)

#ejercicio 8: 
# def calculator(num1, num2):
#     cociente = num1 / num2
#     resto = num1 % num2

#     return {"cociente": cociente, "resto":resto}
# datos = calculator(34, 22)
# print(datos)

#ejercicio 9:
# nombre = input("ingrese su nombre: ")
# apellido = input("ingrese su apellido: ")

# nombre_completo = nombre + " "+ apellido
# print(nombre_completo)

#ejercicio 10:
palabra = input("ingrese una palabra: ")
cant = len(palabra)
print(f"la palabra {palabra} tiene {cant} letras")

#ejercicio 11 (continua con el de arriba)
primeras = palabra[:5]
print(f"las primeras 5 letras de la palabra {palabra} son: {primeras}")

#ejercicio 12 (continua con el de arriba)
def borrarLetra(letra, palabra):
    nueva_palabra = palabra.replace(letra, "")
    return nueva_palabra
letra = input(f"ingrese una letra que desea borrar de la palabra que eligio ({palabra}): .... ")
nueva_palabra = borrarLetra(letra, palabra)
print(f"la plabra quedo asi: {nueva_palabra}")