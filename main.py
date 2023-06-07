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