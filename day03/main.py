'''Día 3. Isla del Tesoro

- 1. Estas en una encrucijada ¿hacia dónde quieres ir izquierda o derecha?
- 2. Si eliges izquierda llegas a un lago si eliges derecha caes en un agujero y ¡fin del juego!
- 3. Si escribes wait esperas un barco, si escribes swim, cruzas nadando y te ataca una trucha ¡fin del juego!
- 4. Si esperaste llegas a la isla ileso encuentras una casa con 3 puertas una roja, una amarilla y una azul elige una
- El rojo es una habitación llena de fuego, el amarillo es donde se encuentra el tesoro, el azul esta llena de cocodrilos'''

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

choice1 = input("Hacia dónde quieres ir escribe izquierda o derecha: ").lower()

if choice1 == "izquierda":
    
    choice2 = input("Has llegado a un lago y hay una isla en medio. Escribe 'wait' para esperar un barco o 'swim' para cruzar nadando: ").lower()

    if choice2 == "wait":
        
        choice3 = input("Haz llegado a la isla. Hay una casa con tres puertas: una roja, una amarilla y una azul. ¿Qué color eliges? ").lower()

        if choice3 == 'roja':
            print("Habitación llena de fuego ¡Fin del juego!")
        elif choice3 == 'amarilla':
            print("Encontraste el tesoro. ¡Haz ganado!")
        elif choice3 == 'azul':
            print("Sala llena de cocodrilos ¡Fin del juego!")
        else: 
            print("Puerta inexiste ¡Fin del juego!")
    else:
        print("Te a atacado una trucha ¡Fin del juego!")
else:
    print("Haz caido en un agujero negro ¡Fin del juego!")