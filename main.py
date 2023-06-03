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



def jugar_golosa():
    objetivo = random.randint(1, 25)
    intentos = 0
    
    print("¡Bienvenido a La Golosa!")
    print("Estoy pensando en un número entre 1 y 25.")
    print("Tu objetivo es adivinarlo en la menor cantidad de intentos.")
    
    
        
        

    
>>>>>>> d9414bf8b498fd3e3b96fe08b76fcb4a07d827b3
print ("hola mundo")