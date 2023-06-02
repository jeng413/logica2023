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
        golosa[1] = " |       | "
    elif intentos == 2:
        golosa[1] = " |      /| "
    elif intentos == 3:
        golosa[1] = " |      /|\\"
    elif intentos == 4:
        golosa[3] = " \\       | "
    elif intentos == 5:
        golosa[3] = " \\      /| "
    elif intentos == 6:
        golosa[3] = " \\      /|\\"
    
    for linea in golosa:
        print(linea)

def dibujar_cara_feliz():
    cara_feliz = [
        "   \\ˆˆˆˆˆˆˆ/",
        "  |  O O  |",
        "  |   ∆   |",
    …

def dibujar_calavera():
    calavera = [
        "    .-''-.",
        "   /       \\",
        "  |         |",
        "  |  R.I.P.  |",
        "  |         |",
        "   \\       /",
        "    `'---'`"
    ]
    
    for linea in calavera:
        print(linea)

def jugar_golosa():
    objetivo = random.randint(1, 25)
    intentos = 0
    
    print("¡Bienvenido a La Golosa!")
    print("Estoy pensando en un número entre 1 y 25.")
    print("Tu objetivo es adivinarlo en la menor cantidad de intentos.")
    
    while True:
        print()
        dibujar_golosa(intentos)
        
        intento = int(input("Ingresa tu número: "))
        intentos += 1
        
        if intento < objetivo:
            print("El número que estás buscando es más grande.")
        elif intento > objetivo:
            print("El número que estás buscando es más pequeño.")
        else:
            print("¡Felicidades! ¡Has adivinado el número en {} intentos!".format(intentos))
            dibujar_cara_feliz()
            break
        
        if intentos == 6:
            print()
            dibujar_golosa(intentos)
            print("¡Lo siento! Has agotado tus intentos.")
            print("El número que estaba buscando era: {}".format(objetivo))
            dibujar_calavera()
            break

    