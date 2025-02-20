#ejercicio 1:
# num = input("ingrese un número entero: ")

# while not num.isnumeric():
#     print("Debe ingresar un número entero....")
#     num = input("ingrese un numero entero: ")

# res_A = "El programa no toma como que es un numero entero a los nums negativos"

#Parte B:
# num = ""

# while type(num) != int:
#     try:
#         num = int(input("Ingrese un numero: "))
#     except ValueError: 
#         print("debe ingresar un numero entero")
#     else:
#         print(f"su numero elegido es: ..... {num}")

#ejercicio 2:

# def solicitar_num(palabra):
#     num = ""
#     while type(num) != int:
#         try:
#             num = int(input(f"{palabra}: "))
#         except ValueError:
#             print("Debe ingresar un numero entero: ")
    
#     return num

# def calcular_producto(num_1, num_2):
#     return num_1 * num_2

# num_1 = solicitar_num("Ingrese un numero")
# num_2 = solicitar_num("Ingrese otro numero")

# producto = calcular_producto(num_1, num_2)

# print(producto)

#ejercicio 3
#tomo como ya creada la funcion anterior:
# print("este programa te va a decir el coiciente entre el divisor y el dividiendo")
# divisor = solicitar_num("ingrese un divisor")
# dividiendo = solicitar_num("ingrese un dividiendo")

# try: 
#     cociente = int(divisor/ dividiendo)
# except ZeroDivisionError:
#     print("no puede calcular") 

# print(cociente)

#ejercicio 4:
# import os 
# directorio_actual = os.path.dirname(__file__)
# ruta_archivo = os.path.join(directorio_actual, "archivos", "files.txt")

# archivo = ""
# try:
#     archivo = open(ruta_archivo, "r")
# except FileNotFoundError:
#     print("no se pudo encontar el archivo")
# else: 
#     print(archivo.read())
# finally: 
#     if archivo:
#         print("cerrando la connexión...")
#         archivo.close()
#     else: print("no hago nada xd")

# print("end")

#ejercicio 5:
# def function(lista, index): 
#     try:
#         valor = lista[index]
#     except IndexError:
#         return "no se pudo encontar el valor"
#     else: 
#         return valor

# lista = [1,4,6,24]
# posicion = function(lista, 50)
# print(posicion)

#ejercicio 6: 
# print("juego de chinchon")
# print("el minimo de juugadores son dos y el maximo cuatro")

# def verificar_num(num):
#     if not (num >= 2):
#         raise Exception("el valor no debe ser menor menor a 2")
#     elif not(num <= 4):
#         raise Exception("el valor no puede ser mayor a 4")


# numero_jugadores = ""
# ciclo = True
# while ciclo:
#     try:
#         numero_jugadores = int(input("ingrese el numero de jugadores: "))
#         verificar_num(numero_jugadores)
#     except ValueError: 
#         print("ingrese un valor valido")
#     except Exception as e:
#         print(e)
#     else: 
#         ciclo = False
#         print(f"el numero de jugadores es {numero_jugadores}")
    
#ejercico 7:
#En Py se valida con except para el caso de las funciones
# def verificar_datos(num):
#       if num < 2:
#           raise Exception("el numero de jugadores tiene que ser mayor a 2")
#       elif num > 6: 
#           raise Exception("el numero de jugadores tiene que ser menor a 6") 
#       elif (num % 2):
#           raise Exception("el numero de jugadores debe ser par")
#       
# def solicitar_numero_jugadores():
#     ciclo = True
#     while ciclo:
#         try:
#             numero_jugadores = int(input("ingrese el numero de jugadores: "))
#             verificar_datos(numero_jugadores)
#         except ValueError:
#             print("ingrese un dato valido")
#         except Exception as e: 
#             print(e)
#         else: 
#             print(numero_jugadores)
#             ciclo = False
#     return numero_jugadores

# num = solicitar_numero_jugadores()
# print("El numero de jugadores es " + num)

#ejercicio 8:
# opciones = {
#     1: "hamburguesas",
#     2: "milanesas",
#     3: "gaseosa",
#     4: "alfajor",
#     5: "papas fritas",
#     6: "agua"
# }

# valores = {
# 1:1000,
# 2:1500,
# 3:500,
# 4:300,
# 5:600,
# 6:350
# }

# lista_diccionarios = []

# #recorro cada elemnot con un for:
# for codigo in range(len(opciones)):
#     codigo += 1
#     opcion = opciones[codigo]
#     valor = valores[codigo]
#     lista_diccionarios.append({"codigo": codigo, "opcion": opcion, "valor": valor})

# #los muestro por pantalla: 
# for menu in lista_diccionarios:
#     print(f"{menu["codigo"]}: {menu["opcion"]} -> {menu["valor"]}")

# Ciclo = True
# while Ciclo: 
#     try:    
#         opcion_usuario = int(input("ingrese una opcion: "))
#         if not any(menu["codigo"] == opcion_usuario for menu in lista_diccionarios):
#             raise Exception("la opcion debe estar en la lista")
#         #verifico que la cantidad sea un numero:
#         cantidad = int(input("ingrese un numero: "))
#     except ValueError:
#         print("el valor debe ser un numero")
#     except Exception as e:
#         print(e)
#     else: 
#         Ciclo = False
#         #obtenfo el producto en la lista:
#         objeto_seleccionado = ""
#         for opcion in lista_diccionarios:
#             print(opcion)
#             if opcion["codigo"] == opcion_usuario:
#                 objeto_seleccionado = opcion
#                 break
#         total = cantidad * objeto_seleccionado["valor"]
#         print(f"total a pagar ${total}")
