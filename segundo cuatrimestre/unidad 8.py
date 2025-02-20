#Cosas Generales: 
import os

# Obtener el directorio actual donde está el archivo 'unidad 8.py'
directorio_actual = os.path.dirname(__file__)
espacio = "\n"
#ejericio 1:

# # Construir la ruta completa hacia 'pregunta.txt' en la carpeta 'archivos'
# ruta_archivo = os.path.join(directorio_actual, "archivos", "pregunta.txt")

# # Abrir el archivo utilizando la ruta construida
# archivo = open(ruta_archivo, "r+")

# texto = archivo.readline()
# print(texto)

# respuesta = input("ingrese su respuesta: ")
# archivo.write(respuesta + "\n")

# archivo.close()

#ejercicio 2:
# import os

# repositorio = os.path.dirname(__file__)
# ruta_archivo = os.path.join(repositorio, "archivos", "ejercicio 2.txt")

# archivo = open(ruta_archivo, "r")

# #leo cada linea del archivo 
# filas = archivo.readlines()

# # cierro el archivo
# archivo.close()

# #modifico las filas (le quito los espacios):
# lista_personas = []
# for persona in filas:
#     lista_personas.append(persona.capitalize().strip())

# print(filas)
# #verifico si esta Santi:
# if "Santi" in lista_personas:
#     print("esta santi")
#     lista_personas.append("Tomas")

# for persona in lista_personas:
#     print(persona)

# #calculo cuanto dindero me tienen que dar:
# cantidad_de_dinero = len(lista_personas) * 1000
# print(f"Ale para hacerle el regalo a Sol ${cantidad_de_dinero}")

#ejercicio 3:
# ruta_archivo = os.path.join(directorio_actual, "archivos", "compras.txt")

# pregunta = input("¿Qué quiere comprar?, ingrese X para finalizar ")

# lista_supermercado = []

# while pregunta.lower() != "x":
#     if len(pregunta) >= 2:
#         lista_supermercado.append(pregunta)
#     else : print("la palbra debe ser mayor igual a 2 letras")
#     pregunta = input("¿Qué quiere comprar?, ingrese X para finalizar ")

# #Guardo los datos en el archivo
# archivo = open(ruta_archivo, "w")

# for elemento in lista_supermercado:
#     archivo.write(elemento + "\n")

# archivo.close()

# #lo leo nuevamente el archivo:
# lectura = open(ruta_archivo, "r")

# lineas = lectura.readlines()
# print(lineas)

# lectura.close()

#ejercicio 4:
# ruta_archivo = os.path.join(directorio_actual, "archivos", "ejercicio 3.txt")

# archivo = open(ruta_archivo, "r")
# datos = archivo.read().lower()

# archivo.close()

# texto_modificado = datos.replace("poco", "mucho")
# print(datos)
# archivo = open(ruta_archivo, "w")
# archivo.write(texto_modificado)

#ejercicio 5:
#tengo que leer el archivo:
# ruta_archivo = os.path.join(directorio_actual, "archivos", "ejercicio 5.csv")

# archivo = open(ruta_archivo, "r")
# data = archivo.readlines()
# archivo.close()
# lista = []

# for i in range(len(data)):
#     separados = data[i].strip().split(";")
#     # print(separados)
#     diccionario = {
#         "Nombre productos": separados[0],
#         "Codigo Producto": separados[1],
#         "Precio por unidad": separados[2],
#         "Stock": separados[3]
#     }
#     lista.append(diccionario)

# #tengo que mostrar cada resultado por si solo, es decir mustro los datos de la lista
# for elemento in range(len(lista)):
#     print(lista[elemento])

# def agregar_a_la_lista(data):
#     #antes de agregarlo tengo que hacer un join
#     #antes de eso como os datos que recibo tienen numeros, necesito pasar todo a str
#     mapa = map(str, data.values())
#     lista_unida = ";".join(mapa)

#     #lo guardo en el archivo:
#     archivo = open(ruta_archivo, "a")
#     archivo.write(lista_unida + "\n")
#     archivo.close()
    

# nuevo_dato = {
#     "Nombre productos": "hojas A4",
#     "Codigo Producto": 35662,
#     "Precio por unidad": 600,
#     "Stock": 45
# }

# agregar_a_la_lista(nuevo_dato)

#ejercicio 6:
# alumnos = [
#     {
#         "nombre" : "juan",
#         "apellido": "de la choya",
#         "dni": 1,
#         "nota": 4
#     },
#         {
#         "nombre" : "markatos",
#         "apellido": "sapenibuslis",
#         "dni": 2,
#         "nota": 9
#     },
#         {
#         "nombre" : "la katos",
#         "apellido": "del valle de  katamarka",
#         "dni": 3,
#         "nota": 3
#     }
# ]

# def guardar_notas(alumno):
#     print(alumno)

#     datos_unidos = ";".join(map(str, alumno.values()))
#     print(datos_unidos)
    
#     ruta_archivo = os.path.join(directorio_actual, "archivos", "notas.csv")
#     archivo = open(ruta_archivo, "a")
#     archivo.write(datos_unidos + "\n")
#     archivo.close()

# def verificar_aprobacion():
#     ruta_archivo = os.path.join(directorio_actual, "archivos", "notas.csv")
#     archivo = open(ruta_archivo, "r")
#     alumnos = archivo.readlines()

#     alumnos_aprobados = []

#     for alumno in alumnos:
#         datos_separados = alumno.strip().split(";")

#         nombre = datos_separados[0]
#         apellido = datos_separados[1]
#         dni = datos_separados[2]
#         nota = int(datos_separados[3])

#         if nota >= 4:
#             info_alumno = {
#                 "nombre": nombre,
#                 "apellido": apellido,
#                 "dni": dni,
#                 "nota":  nota
#             }
#             alumnos_aprobados.append(info_alumno)
    
#     return alumnos_aprobados

# #Punto A
# for alumno in alumnos:
#     guardar_notas(alumno)

# #Punto B
# aprobados = verificar_aprobacion()

# print("aprobados.....")
# print(aprobados)

#ejercicio 7: 
# ruta_archivo_salas = os.path.join(directorio_actual, "archivos", "salas.txt")
# ruta_archivo_peliculas = os.path.join(directorio_actual, "archivos", "peliculas.txt")
# ruta_archivo_funciones = os.path.join(directorio_actual, "archivos", "funciones.csv")

# salas = open(ruta_archivo_salas, "r", encoding="utf-8")
# salas_info  = salas.readlines()
# salas.close()

# peliculas = open(ruta_archivo_peliculas, "r", encoding="utf-8")
# peliculas_info = peliculas.readlines()
# peliculas.close()

# #"Uso zip() que sirve para unbir 2 o más funciones en un for"
# funciones = open(ruta_archivo_funciones, "a", encoding="utf-8")

# for sala, pelicula in zip(salas_info, peliculas_info):

#     data = ";".join([sala.strip(),pelicula.strip()])
#     funciones.write(data + espacio)

# funciones.close()

#Ejercicio 8:
ruta_archivo = os.path.join(directorio_actual, "archivos", "ejercicio 8.csv")
ruta_archivo_txt = os.path.join(directorio_actual, "archivos", "ejericio 8.txt")

archivo = open(ruta_archivo, "r", encoding="utf-8")
datos = archivo.readlines()
archivo.close()

archivo_txt = open(ruta_archivo_txt, "a", encoding="utf-8")

for dato in datos:
    persona = dato.strip().split(";")

    texto = f"a {persona[0]} {persona[2]} le gusta el {persona[1]}"
    archivo_txt.write(texto + espacio)

archivo_txt.close()