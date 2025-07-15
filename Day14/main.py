import os
import random
from art import logo, vs
from game_data import data

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def formatear_datos(cuenta):
    nombre = cuenta["name"]
    descripcion = cuenta["description"]
    pais = cuenta["country"]
    return f"{nombre}, {descripcion}, de {pais}"

def es_correcta(a, b, eleccion):
    if a > b:
        return eleccion == "a"
    else:
        return eleccion == "b"

def juego():
    limpiar()
    print(logo)
    puntuacion = 0
    continuar = True
    cuenta_b = random.choice(data)

    while continuar:
        cuenta_a = cuenta_b
        cuenta_b = random.choice(data)
        
        while cuenta_a == cuenta_b:
            cuenta_b = random.choice(data)

        print(f"Compara A: {formatear_datos(cuenta_a)}")
        print(vs)
        print(f"Contra B: {formatear_datos(cuenta_b)}")

        eleccion = input("¿Quién tiene más seguidores? Escribe 'A' o 'B': ").lower()
        
        seguidores_a = cuenta_a["follower_count"]
        seguidores_b = cuenta_b["follower_count"]
        correcta = es_correcta(seguidores_a, seguidores_b, eleccion)

        limpiar()
        print(logo)
        
        if correcta:
            puntuacion += 1
            print(f"¡Correcto! Tu puntuación actual es: {puntuacion}.\n")
        else:
            print(f"¡Incorrecto! Tu puntuación final es: {puntuacion}.")
            continuar = False

juego()