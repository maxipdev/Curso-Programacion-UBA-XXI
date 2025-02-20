#ejercicio 7: 

def estaciones(letra):
    letra = letra.lower()

    if letra == "v": print("Verano")
    elif letra == "o": print("Otoño")
    elif letra == "i": print("Invierno")
    elif letra == "p": print("Primavera")
    else : print("“error”")

print("Ingrese las letras una por línea:")
print("V para verano, O para otoño, I para invierno, P para primavera")

estaciones(input("ingrese una letra: ..."))