#ejercio 4: 

print("ingrese su año de nacimiento y un año aleatorio para determinar cuatos años tenia ese año")
año_de_nacimiento = int(input("ingrese su año de nacimiento: "))
otro_año = int(input("ingrese otro año: "))

calc = otro_año - año_de_nacimiento

if calc < 1: 
    print(f"usted todavia no nació en el año {otro_año}")
else: 
    print(f"su edad en el año {otro_año} era: {calc}")