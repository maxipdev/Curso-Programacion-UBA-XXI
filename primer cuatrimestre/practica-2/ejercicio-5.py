#ejercicio 5

print("ingrese 5 enteros para determinar su promedio")
cantidad_de_enteros = 5
suma_total = 0

for l in range(cantidad_de_enteros):
    valor = input("ingrese un entero: ")

    #se elimina el - adelante de los numeros asi se evalua que sea un digito
    while not valor.lstrip('-').isdigit(): 
        print("error, intenete nuevamente...")
        valor = input("ingrese un entero: ")

    num = int(valor)
    suma_total += num

print(suma_total)
print(f"el promedio de los números que ingreso es de: {suma_total / cantidad_de_enteros}")