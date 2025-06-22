'''Día 4. Piedra, Papel, Tijera: 

- Pregunta al usuario su elección: 

* 0 = piedra 
* 1 = papel 
* 2 = tijera

- El ordenador elige de forma aleatoria '''

import random

usuario = int(input("¿Qué eliges? Escribe 0 para piedra, 1 para papel o 2 para tijera:\n"))
computadora = random.randint(0, 2)

piedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

tijeras = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

opciones = [piedra, papel, tijeras]

print(f"\nComputadora eligió:\n{opciones[computadora]}")
print(f"\nTú elegiste:\n{opciones[usuario]}")

if computadora == usuario:
    print("¡Es un empate!")
elif (computadora == 0 and usuario == 2) or (computadora == 1 and usuario == 0) or (computadora == 2 and usuario == 1):
    print("¡Gana la computadora!")
else:
    print("¡Tú ganas!")