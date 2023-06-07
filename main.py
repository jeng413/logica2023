<<<<<<< HEAD
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

=======
<<<<<<< HEAD
  if intentos == 0:
=======
 import random

def dibujar_golosa(intentos):
    golosa = [
        "   -----   ",
        " /       \\ ",
        " |       |  ",
        " \\       / ",
        "   -----    ",
    ]
    
    if intentos == 0:
>>>>>>> d9414bf8b498fd3e3b96fe08b76fcb4a07d827b3
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
<<<<<<< HEAD
        golosa[3] = " \\      /|\\"
=======
        golosa[3] = " \\      /|\\"
    
    for linea in golosa:
        print(linea)



>>>>>>> 24006483e6e75e486696aa892c1b81a03ca6547f
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