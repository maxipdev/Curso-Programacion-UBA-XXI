#ejercico 4: 
def valor_absoluto(numero): 
    if numero < 0:
        return -numero
    else : return numero

user_number = int(input("ingrese un numero: "))

resultado = valor_absoluto(user_number)

print(resultado)

#ejercicio 5: 
print("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T)")
letra  = input("elige una letra: ")

while letra not in ["r", "p", "t"]:
    print("error la letra que ingreso está mal")
    letra  = input("elige nuevamenete una letra: ")

letra = letra.lower()
print(f"usted: {letra}")
print("maquina: ")
if letra == "r":
    print("Piedra (R)")
elif letra == "p": 
    print("Papel (P)")
elif letra == "t":
    print("Tijera (T)")

print("te gane!!!!!!!!!!!!!!!!!!")