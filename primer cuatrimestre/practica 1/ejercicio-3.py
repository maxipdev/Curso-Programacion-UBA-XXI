#ejercicio 3: 

people = [
    {"name": "maria", "typePerson": "friend"},
    {"name": "juan", "typePerson": "cousin"},
    {"name": "carlos", "typePerson": "mother"},
    {"name": "marta", "typePerson": "uncle"},
    {"name": "julio", "typePerson": "friend"},
    {"name": "cesar", "typePerson": "aunt"},
    {"name": "sebastian", "typePerson": "brother"},
    {"name": "alexa", "typePerson": "sister"}
]



for person in people: 
    texto_de_invitacion = f"Hola {person["name"]}, {person["typePerson"]} estas invitado/a a mi cumpleaños el dia 27/4. Te espero no faltes!!"
    print(texto_de_invitacion)

print("Termino el prgrama")