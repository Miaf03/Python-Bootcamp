# Día 3. Isla del Tesoro: https://ascii.co.uk/art Nuestra misión es encontrar el tesoro

# Estas en una encrucijada ¿hacia dónde quieres ir izquierda o derecha
# Si eliges izquierda llegas a un lago donde hay una isla en medio de todo
# Si escribes wait esperas un barco, si escribes swim, cruzas nadando 
# Si esperaste llegas a la isla ileso encuentras una casa con 3 puertas una roja, una amarilla y una azul elige una
# El rojo es una habitación llena de fuego, el amarillo es donde se encuentra el tesoro, el azul esta llena de cocodrilos

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("¡Bienvenido a la Isla del Tesoro!")
print("Tu misión es encontrar el tesoro")

choice1 = input("Estás en una encrucijada hacia dónde quieres ir escribe izquierda o derecha: ").lower()

if choice1 == "izquierda":
    choice2 = input("Has llegado a un lago, hay una isla en medio. Escribe 'esperar' para esperar un barco o 'nadar' para cruzar nadando: ").lower()

    if choice2 == "esperar":
        choice3 = input("Llegas a la isla sin sufrir daño. Hay una casa con tres puertas: una roja, una amarilla y una azul. ¿Qué color eliges? ").lower()

        if choice3 == 'roja':
            print("Es una habitación llena de fuego ¡Fin del juego!")
        elif choice3 == 'amarilla':
            print("Encontraste el tesoro. ¡Ganaste!")
        elif choice3 == 'azul':
            print("Entras en una sala llena de cocodrilos ¡Fin del juego!")
        else: 
            print("Eliges una puerta que no existe ¡Fin del juego!")
    else:
        print("Te atacó una trucha enojada ¡Fin del juego!")

else:
    print("Caíste en un agujero ¡Fin del juego!")