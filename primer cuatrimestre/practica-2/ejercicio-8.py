#ejercicio 8

def numeros(numero_1, numero_2):
    resto = numero_1 % numero_2
    cociente = numero_1 / numero_2

    return resto, cociente

[resto, cociente] = numeros(2, 1)
print("resto: ", resto)
print("cociente: ", cociente)