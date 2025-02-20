#ejericio 1:
# print("programa que demuestra si un número es más grande que otro, para ello se tienen que escribir 2 números y de alli se comprobará")
# num_1 = input("ingrese un numero: ")

# while not num_1.isdigit():
#     print("tiene que ingresar un numero")
#     num_1 = input("ingrese nuevamente un número: ")

# num_2 = input("ingrese otro numero: ")

# while not num_2.isdigit():
#     print("tiene que ingresar un numero")
#     num_2 = input("ingrese nuevamente un número: ")
# #Esto marca si es mas grande o no en un booleano
# result = False

# if num_1 > num_2 : 
#     print(f"El número {num_1} es mayor al número {num_2}")
#     result = True
# else :
#     print(f"El número {num_1} es menor al número {num_2}")
# print(f"respuesta en booleano: {result}")

#ejercicio 2:
# print("programa que determina si una letra pertene a las vocales")
# letra = input("ingrese una letra: ")

# vocales = "aeiou"

# if letra.lower() not in vocales:
#     print(f"la letra {letra} no pertene a las vocales")
# else :
#     print(f"la letra {letra} si petenece a las vocales")

#ejercicio 3:
# num = input("ingrese un número: ")

# while not num.isdigit():
#     num = input("ingrese un número: ")

# num = int(num)
# #determino si el núm es par o impar:
# if num %2 == 0:
#     if (num < 10):
#         print(f"el numero {num} es par y es menor a 10")
#     else: print("el numero es par pero no menor a 10")
# else :
#     print("el numero no es par")

# #otra interpretacion del ejercicio pudo haber sido: 
# if num %2 == 0 and num < 10:
#     print("el numero es par y menor a 10")
# else : print("el numero no es par")

#ejercico 4:
# def valor_absoluto(num) :
#     if num < 0:
#         return -num
#     else : return num

# num = int(input("ingrese un numero: "))
# result = valor_absoluto(num)
# print(result)

# #ejercicio 5:
# print("juego de piedra, papel y tijera:")
# print("para jugar tienes que ingresar un letra, R (piedra) o T (tijera) o P (papel)")
# letras_disponibles = ("p", "r", "t")

# letra = input("ingrese una letra: ")
# letra = letra.lower()
# while letra not in letras_disponibles: 
#     print("tenés que ingresar una letra valida")
#     print("R (piedra) o T (tijera) o P (papel), volve a intentar..")
#     letra = input("ingrese una letra: ")

# print (f"tu letra: {letra}")
# if letra == "p":
#     print("letra pc: T (tijera)")
# elif letra == "r":
#      print("letra pc: P (papel)")
# else :  print("letra pc: R (piedra)")

# print("Te Gane!!!")
    
#ejercicio 6:
# num1 = int(input("ingrese un numero: "))
# num2= int(input("ingrese otro numero: "))

# suma = num1 + num2
# limite = 100

# if suma < limite: 
#     distancia = limite - suma
#     print(f"le falta para llegar {limite} {distancia}")
# else: print(f"llega a {limite}")

#ejercicio 7:
# def verificador_estaciones(letra):
#     letra = letra.lower()
#     if letra == "p":
#         return "Primavera"
#     elif letra == "v":
#         return "verano"
#     elif letra == "o":
#         return "otoño"
#     elif letra == "i":
#         return "invierno"
#     else : return "Error"

# print("ingresa una letra para ver en que estacion te encuentras...")
# print("V para verano, O para otoño , I para invierno y P para primavera")
# letra = input("ingrese una letra: ")
# estacion = verificador_estaciones(letra)
# print(estacion)

#ejercicio 8:
# def contrador(num):
#     num  = int(num)
#     for i in range(1, num + 1):
#         print(i)

# num = input("ingrese un numero entero positivo: ")
# while not num.isdigit():
#     num = input("ingrese un numero entero positivo: ")

# contrador(num)

#ejercicio 9:
# def tablas(num):
#     num = int(num)
#     print(f"La tabla del {num}")
#     for i in range(1, 10 + 1):
#         calculo = num * i
#         print(f"{num} X {i} = {calculo}")

# num = input("ingrese un número para ver su tabla: ")
# tablas(num)

# #ejercicio 10: 
# num = int(input("ingrese un numero: "))

# for i in range(num): 
#     print(f"{i} Que los cumplas feliz")

#ejercicio 10: 
# def negocio(moto_cobrar):
#     moto_cobrar = int(moto_cobrar)
#     pagado= int(input("ingrese cuanto pago: "))

#     suma_parcial = pagado

#     if suma_parcial == moto_cobrar:
#         print("listo")
#     else: print("falta")
    
#     while not suma_parcial == moto_cobrar:
#         print(f"le falta pagar {moto_cobrar - suma_parcial}")
#         print("vuelva a ingresar otro pago")
#         pagado= int(input("ingrese cuanto pago: "))
#         suma_parcial += pagado
#         print(f"nuevo suma parcial: {suma_parcial}")
    
#     print("listo, pagado exitosamente")

# negocio(input("ingrese el monto a cobrar: "))

#ejercicio 11:
# print("programa que determina si los numero son pares o impares: ")
# for i in range(1, 20 + 1):
#     if i % 2 == 0: 
#         print(f"El número {i} es par")
#     else : print(f"El número {i} es impar")

#ejercicio 12: A
# precio = int(input("ingrese el precio de la maquina: "))
# print("la letra F representa 1 ficha, para jugar tiene que ingresar la cantidad de fichas correspondientes")

# for i in range(1, precio + 1):
#     if i == 1 : 
#         ficha = input("ingrese una ficha: ")
#     else : ficha = input("ingrese otra ficha: ")

#     print(ficha)
#     while not ficha.lower() == "f":
#         ficha = input("ingrese una ficha valida: ")
# print("A jugar")

#ejercicio 12 B y C:
precio = int(input("ingrese el precio de la maquina: "))
print("la letra F representa 1 ficha, para jugar tiene que ingresar la cantidad de fichas correspondientes")
print("solo puedes ingreesar de a una ficha")
print(f"precio: {precio}")
fichas_ingresadas = 0

ficha = input(f"ingrese {precio} fichas para comenzar: ")

if ficha.lower() == "f":
    print("ficha correcta")
    fichas_ingresadas += 1
else : print("Por favor solamente ingrese fichas reales (F)")

while not fichas_ingresadas == precio: 
    ficha = input(f"ingrese {precio - fichas_ingresadas} para comenzar: ")
    if ficha.lower() == "f":
        print("ficha correcta")
        fichas_ingresadas += 1
    else : print("Por favor solamente ingrese fichas reales (F)")
print("A Jugar!")

#ejericio 14: 
#(no lo se hacer.... :(  )