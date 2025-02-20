#ejercio 3: 

print("programa para determinar si el número que ingresa es entero")
num = input("ingrese un número entero: ")

while not num.isdigit(): 
    num = input("ingrese un número entero: ")

num = int(num)
value = num % 2

if value == 0:
    print(f"número {num} es par")
else: 
    print(f"número {num} es impar")