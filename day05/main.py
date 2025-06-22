'''Día 5. Generador de contraseñas: Pregunta al usuario cuántas letras, simbolos y números quiere en su contraseña'''

import random

print("Bienvenido al generador de PyPassword!")

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
simbolos = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

cantidad_letras = int(input("Cuántas letras quieres en tu contraseña: "))
cantidad_simbolos = int(input("Cuántos simbolos quieres en tu contraseña: "))
cantidad_numeros = int(input("Cuántos números quieres en tu contraseña: "))

contraseña = []

for _ in range(cantidad_letras):
    contraseña.append(random.choice(letras))

for _ in range(cantidad_simbolos):
    contraseña.append(random.choice(simbolos))

for _ in range(cantidad_numeros):
    contraseña.append(random.choice(numeros))

random.shuffle(contraseña)

contraseña_final = "".join(contraseña)
print(f"Tu contraseña generada es {contraseña_final}")