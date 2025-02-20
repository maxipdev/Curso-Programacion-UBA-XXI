#ejercicio 6 funciones: 

def numeros(numero): 
    num_anterior = numero - 1
    num_siguiente = numero + 1

    print("numero: ", numero)
    print("numero anterior: ", num_anterior)
    print("numero siguiente ", num_siguiente)

user_number = input("ingrese un número: ")

while not user_number.isdigit():
    print("Error, pruebe otra vez")
    user_number = input("ingrese un número: ")

numeros(int(user_number))