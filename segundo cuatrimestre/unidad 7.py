#ejercicio 1:
#Creo el diccionario, punto A
# estudiante = {
#     "nombre": "Juan Pérez",
#     "dni": "12345678",
#     "edad": 16,
#     "email": "juan.perez@gmail.com"
# }

# #Punto B: (Agrego el nuevo diccionario)
# estudiante["curso"] = {
#     "año": 4,
#     "división": "B",
#     "orientación": "Ciencias Naturales"
# }

# #Punto C (Creo una lista de todos los estudiantes)

# lista_estudiantes = [
#     {
#         "nombre": "Juan Pérez",
#         "dni": "12345678",
#         "edad": 16,
#         "curso": {"año": 4, "división": "B", "orientación": "Ciencias Naturales"}
#     },
#     {
#         "nombre": "María López",
#         "dni": "87654321",
#         "edad": 18,
#         "curso": {"año": 6, "división": "A", "orientación": "Economía"}
#     },
#     {
#         "nombre": "Carlos Gómez",
#         "dni": "12349876",
#         "edad": 17,
#         "curso": {"año": 5, "división": "C", "orientación": "Arte"}
#     }
# ]

# #Busco las personas con mayor edad:
# mas_grande = max(lista_estudiantes, key=lambda x: x["edad"])
# print(mas_grande)

#ejercicio 2:
# lista_de_plantas = []

# def agregar_plantas(datos):
#     #añado la planta a la lista de plantas:
#     lista_de_plantas.append(datos)

# #ingresar nueva planta:
# nueva_planta = {"precio": 200, "especie": "rosa", "luz": True}
# agregar_plantas(nueva_planta)
# print(f"lsita de plantas: {lista_de_plantas}")

#ejercicio 3: 
# ticket = [
#     {
#         "nombre del producto": "Galletitas tu vieja",
#         "precio por unidad": 15,
#         "cantidad": 50
#     },
#         {
#         "nombre del producto": "tu concha es la mas rica",
#         "precio por unidad": 200,
#         "cantidad": 1
#     },
#         {
#         "nombre del producto": "las bolas peludas de tu abuelo",
#         "precio por unidad": 2,
#         "cantidad": 369
#     },
#         {
#         "nombre del producto": "la masa que se estira como las tetas de tu abuela",
#         "precio por unidad": 34,
#         "cantidad": 56
#     },
# ]

# #hago una funcion que recibe el ticket y te dice cuanto tenes que pagar:
# def cantidad_pagar(ticket):
#     total = 0
#     for elemento in ticket:
#         cantidad = elemento["cantidad"]
#         precio = elemento["precio por unidad"]

#         total += precio * cantidad

#     return total

# total_a_pagar = cantidad_pagar(ticket)
# print(f"el total a pgar es de ${total_a_pagar}")

#ejercicio 4: 
# Lista de diccionarios con series
# series = [
#     {
#         "nombre": "Breaking Bad",
#         "año": 2008,
#         "puntuación": 10
#     },
#     {
#         "nombre": "Stranger Things",
#         "año": 2016,
#         "puntuación": 4
#     },
#     {
#         "nombre": "Game of Thrones",
#         "año": 2011,
#         "puntuación": 8
#     },
#     {
#         "nombre": "The Office",
#         "año": 2005,
#         "puntuación": 6
#     },
#     {
#         "nombre": "Chernobyl",
#         "año": 2019,
#         "puntuación": 2
#     }
# ]

# #hago una función que reciba el diccinario y devulva las mejores peliculas (las que ella recomienda)
# def selector_de_peliculas(series):
#     mejores_peliculas = []
#     for serie in series:
#         if serie["puntuación"] > 7:
#             mejores_peliculas.append(serie)
#     return mejores_peliculas

# peliculas_que_recomienda = selector_de_peliculas(series)
# print(f"las mejores peliculas que recomienda Sol son: {peliculas_que_recomienda}")

#ejercicio 5:
# alumnos = [
#     {
#         "nombre": "apolorodo",
#         "apellido": "nicotatopulos",
#         "intento": 3,
#         "nota": 4
#     },
#         {
#         "nombre": "maria",
#         "apellido": "de la jumepatilla",
#         "intento": 2,
#         "nota": 6
#     },
#         {
#         "nombre": "francola",
#         "apellido": "ricca",
#         "intento": 1,
#         "nota": 9
#     },
# ]

# #como pide establecer las notas en cualquier intento:
# def promedio(alumnos, intento):
#     alumnos_promocionados = []
#     for a in  alumnos:
#         if a["intento"] == intento:
#             #calculo el promedio
#             promedio = a["nota"]/2
#             #Actualizo los datos del alumno:
#             a.update({"promedio": promedio})
#             #cargo los datos del alumno en la nueva lista
#             alumnos_promocionados.append(a)
#     return alumnos_promocionados 

# #solicito al usuario cual es el intento quq quiere evaluar:
# intento = int(input("ingrese el intento: "))
# alumnos_promocionados = promedio(alumnos, intento)
# print(f"alumnos promocionados: {alumnos_promocionados}")

#ejercicio 6: 
# productos = [
#     {
#         "codigo": 23,
#         "fecha de vencimiento": "17/08/24",
#         "paso calidad": True
#     },
#         {
#         "codigo": 34424256,
#         "fecha de vencimiento": "1/12/30",
#         "paso calidad": True
#     },
#         {
#         "codigo": 4,
#         "fecha de vencimiento": "12/10/22",
#         "paso calidad": False
#     },
#         {
#         "codigo": 56098,
#         "fecha de vencimiento": "19/04/20",
#         "paso calidad": True
#     },
#         {
#         "codigo": 156431,
#         "fecha de vencimiento": "23/11/06",
#         "paso calidad": False
#     },
# ]

# #tengo que devolver lso productos que no pasaron la calidad en una tupla 
# def verificador_de_calidad(productos):
#     productos_eliminados_lista = []
#     #cree una copia de la lista "productos" para evitar problemas en la iteracion
#     for p in productos[:]:
#         if p["paso calidad"] == False:
#             #elimino los productos que no pasaron el chequeo
#             productos.remove(p)
#             #añado a la lista de los productos_eliminados_lista: 
#             productos_eliminados_lista.append(p)
#     #como se quiere una tupla paso la lista a tupla
#     productos_eliminados_tupla = tuple(productos_eliminados_lista)
#     return productos_eliminados_tupla


# productos_eliminados = verificador_de_calidad(productos)
# print(f"los productos elimiandos son: {productos_eliminados}")

# #Hago esto para mostar como quedaron los productos despues de la modificación
# print("Codigo, fecha, calidad")
# for products in range(len(productos)):
#     print(f"producto N°{products + 1}")

#     codigo = productos[products]["codigo"]
#     fecha = productos[products]["fecha de vencimiento"]
#     calidad = productos[products]["paso calidad"]

#     print(codigo, fecha, calidad)
#     print("   ")

#ejercicio 7:
participantes = [
    {
        "dni": 1,
        "nombre": "juan carlos",
        "maratones": [
            {
                "año": 2024,
                "puesto": 20,
                "tiempo (minutos)": 53,
                "nombre": "paris"
            },
           {
               "año": 2023,
                "puesto": 70,
                "tiempo (minutos)": 103,
                "nombre": "frankfurt"
            },
            {
                "año": 2022,
                "puesto": 3,
                "tiempo (minutos)": 44,
                "nombre": "barcelona"
            }
        ]
    },
    {
        "dni": 2,
        "nombre": "Francisco Franco",
        "maratones": [
            {
                "año": 2024,
                "puesto": 23,
                "tiempo (minutos)": 55,
                "nombre": "paris"
            },
            {
                "año": 2023,
                "puesto": 104,
                "tiempo (minutos)": 163,
                "nombre": "frankfurt"
            },
            {
                "año": 2022,
                "puesto": 77,
                "tiempo (minutos)": 90,
                "nombre": "barcelona"
            }
        ]
        }
    ]


#respondo pregunta A:
#el campo que guarda todas las maratones es una lista, y la maraton en si es un diccionario

#Ordeno alfabeticamente a los maratonistas: (Pregunta B)
participantes.sort(key=lambda x: x["nombre"])
print(participantes)

#ordeno el tiempo de carrera de cada maratonista: (Pregunta C):
for maratonista in participantes: 
    maratonista["maratones"].sort(key=lambda x: x["tiempo (minutos)"])

