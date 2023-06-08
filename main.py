import random

def dibujar_golosa(intentos):
    golosa = [
        "   -----   ",
        " /       \\ ",
        " |       | ",
        " \\       / ",
        "   -----   "
    ]
    
    if intentos == 0:
        golosa[2] = " |       O "
    elif intentos == 1:
        golosa[3] = " |       | "
    elif intentos == 2:
        golosa[3] = " |      /| "
    elif intentos == 3:
        golosa[3] = " |      /|\\"
    elif intentos == 4:
        golosa[4] = " \\       | "
    elif intentos == 5:
        golosa[4] = " \\      /  "
    elif intentos == 6:
        golosa[4] = " \\      / \\"
    
    for linea in golosa:
        print(linea)

def dibujar_cara_feliz():
    cara_feliz = [
        "  \\ˆˆˆˆˆˆˆ/",
        "  |  O O  |",
        "  |   ∆   |",
        "    \\___/"
    ]
    
    for linea in cara_feliz:
        print(linea)

def dibujar_calavera():
    calavera = [
        "    .-''-.",
        "   /       \\",
        "  |         |",
        "  |  R.I.P. |",
        "  |         |",
        "   \\       /",
        "    `'---'`"
    ]
    
    for linea in calavera:
        print(linea)

def jugar_golosa():
    print("¡Bienvenido a La Golosa!")
    print("¡Gira la ruleta para obtener tu número de vidas!")
    
    while True:
        ruleta = input("Presiona 'R' para girar la ruleta: ")
        
        if ruleta.upper() == "R":
            num_vidas = random.randint(1, 8)
            print("¡Has girado la ruleta! Tienes {} vidas.".format(num_vidas))
            break
        else:
            print("Ingresa 'R' para girar la ruleta.")
    
    objetivo = random.randint(1, 100)
    intentos = 0
    
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tu objetivo es adivinarlo en la menor cantidad de intentos.")
    
    while True:
        print()
        dibujar_golosa(intentos)
        
        intento = input("Ingresa tu número ('H' para obtener una pista): ")
        
        if intento.upper() == "H":
            pista = "El número objetivo es aproximadamente {}".format(objetivo)
            print(pista)
            continue
        
        try:
            intento = int(intento)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
            continue
        
        intentos += 1
        
        if intento < objetivo:
            print("El número que estás buscando es más grande.")
        elif intento > objetivo:
            print("El número que estás buscando es más pequeño.")
        else:
            print("¡Felicidades! ¡Has adivinado el número en {} intentos!".format(intentos))
            dibujar_cara_feliz()
            break
        
        if intentos == num_vidas:
            print()
            dibujar_golosa(intentos)
            print("¡Lo siento! Has agotado tus intentos.")
            print("El número que estaba buscando era: {}".format(objetivo))
            dibujar_calavera()
            break

jugar_golosa()