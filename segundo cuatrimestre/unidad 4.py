#ejericio 1: 
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista[4])

#ejercicio 2: 
# print(len(lista))

#ejercicio 3: 
# lista_distintos =  [1, 4, 10 ,33, 5, 28]

# max = max(lista_distintos)
# min = min(lista_distintos)

# print(max ,min)

#ejercicio 4: 
# lista_ordenada = sorted(lista_distintos)
# print(lista_ordenada)

#ejercicio 5: 
# datos = ("maximo", 18)
# print(f"nombre: {datos[0]}, edad: {datos[1]}")

#ejercicio 6: 
#Punto A
nombres = ["máximo", "milagros", "valentina", "aldana", "ariel"]

nombres[-1] = "juan"
print(nombres)

#Punto B
longitud = len(nombres)
print(longitud - 2)
posicion_querida = longitud - 3
print(nombres[posicion_querida])

#Punto C
for n in nombres:
    print(n)

#Punto D
lista_nueva = nombres * 3
print(lista_nueva)