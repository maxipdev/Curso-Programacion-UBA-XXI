#ejercicio 6:
limite = 100

num_1= input("Ingrese un número entero: ")
num_2= input("Ingrese otro número entero: ")

while not num_1.lstrip('-').isdigit():
    print("cliclo 1")
    print("Error, pruebe otra vez")
    num_1= input("Ingrese un número entero: ")

while not num_2.lstrip('-').isdigit():
    print("cliclo 2")
    print("Error, pruebe otra vez")
    num_2= input("Ingrese un número entero: ")

num_1 = int(num_1)
num_2 = int(num_2)

suma = num_1 + num_2

if suma < limite: 
   diferencia = limite - suma
   print(f"le falta para llegar a {limite}: {diferencia}")
else: 
    print("Llega a 100")