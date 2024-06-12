import random

opciones = ["Tijeras", "Piedras", "Papel"]

def juego(puntaje):
    print("Bienvenido al juego de Piedra, Papel o Tijeras")
    print("Selecciona una opción:")
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")
    opcion = int(input("Opción: "))
    #Validar la respuesta del usuario correcta
    if opcion < 1 or opcion > 3:
        print("Opción inválida, Por favor selecciona una opción válida")
        return
    print(f"Tu elección: {opciones[opcion-1]}")

    #Eleccion de la Maquina
    eleccion_pc = random.choice(opciones)
    print(f"Elección de la PC: {eleccion_pc}")
    
    if eleccion_pc == opciones[opcion-1]:
        print("Empate")
    elif eleccion_pc == "Tijeras" and opciones[opcion-1] == "Piedras":
        print("Ganaste")
        puntaje += 1
    elif eleccion_pc == "Piedras" and opciones[opcion-1] == "Papel":
        print("Ganaste")
        puntaje += 1
    elif eleccion_pc == "Papel" and opciones[opcion-1] == "Tijeras":
        print("Ganaste")
        puntaje += 1
    else:
        print("Perdiste")
    
    print(f"Puntuación: {puntaje}")

    print("¿Quieres jugar de nuevo?")
    print("1. Si")
    print("2. No")
    respuesta = int(input("Respuesta: "))
    if respuesta == 1:
        juego(puntaje)
    else:
        print("Gracias por jugar")
        return
    
        
puntaje = 0
puntaje = juego(puntaje)