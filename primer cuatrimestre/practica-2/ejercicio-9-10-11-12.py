#ejercicio 9:
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")

print(apellido + " " + nombre)

print()
#ejercicio 10:
print("ejercicio 10: ingrese una plabra para determinar la catidad de letras")
palabra = input("ingrese una plaabra: ")
print(len(palabra))

print()
#ejercicio 11:
print("ejercicio 11: Obtener una palabra e imprimir los primeros 5 caracteres")
palabra = input("ingrese una plaabra: ")

palabra_recortada = palabra[0:5]
print(palabra_recortada)

print()
#ejercicio 12:
print("ejercicio 12: Eliminar todas las 'a' de una palabra")
palabra = input("Ingrese una palabra: ")

palabra_sin_a = palabra.replace("a", "")
print(f"palabra original: {palabra}, y sin la a, {palabra_sin_a}")