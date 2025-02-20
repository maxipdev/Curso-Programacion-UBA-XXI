#Ejercico 2

print("vamos a crear un programa, para ello ingresa 2 números enteros a continuación")
numeros_obtenidos = []
for numeros in range(0, 2): 
    numero = input("Ingrese un numero entero: ")
    while not numero.isdigit():
        print(f"{numero} no es un número entero, por favor ingrese un número entero")
        numero = input("Ingrese un numero entero: ")

    numeros_obtenidos.append(int(numero))

print(numeros_obtenidos)

suma = numeros_obtenidos[0] + numeros_obtenidos[1]
resta = numeros_obtenidos[0] - numeros_obtenidos[1]
mult = numeros_obtenidos[0] * numeros_obtenidos[1]
div = numeros_obtenidos[0] / numeros_obtenidos[1]

print("suma: ", suma)
print("resta: " , resta)
print("mult: " , mult)
print("div: " , div)


