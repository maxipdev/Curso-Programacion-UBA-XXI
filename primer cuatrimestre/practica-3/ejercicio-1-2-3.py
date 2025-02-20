#Ejercicio 1:

num = int(input("ingrese un numero: "))
num_2 = int(input("ingrese otro número: "))

resultado = num > num_2
print(resultado)

#ejercicio 2: 
letra  = input("Ingrese una letra: ")

resultado = letra.lower() in ["a", "e", "i", "o", "u"]

if resultado :
    print(f"{letra}, es una vocal")
else : print(f"{letra} no es una vocal")

#ejercicio 3: 
num = int(input("ingrese un numero: "))
if (num / 2 == 0) and (num < 10): 
    print(f"el numero {num} es par y es menor a 10")
else : print(f"el numero no es par")