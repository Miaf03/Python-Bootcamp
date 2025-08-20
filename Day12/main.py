'''Día 12. Adivina el número:

- El juego elige un número aleatorio entre 1 y 100.
- El usuario debe adivinar el número correcto.
- Puede elegir entre dos niveles de dificultad: 'easy' (10 intentos) o 'hard' (5 intentos).
- Después de cada intento, se indica si el número es demasiado alto o demasiado bajo.
- El juego termina cuando el usuario adivina el número o se queda sin intentos.'''

import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_guess(guess, secret_number, attempts_left):
    """Verifica el número ingresado y devuelve el número de intentos restantes."""
    
    if guess > secret_number:
        print("Demasiado alto.")
        return attempts_left - 1
    elif guess < secret_number:
        print("Demasiado bajo.")
        return attempts_left - 1
    else:
        print(f"¡Felicidades! Adivinaste el número {secret_number}")
        return 0

def set_difficulty():
    """Devuelve el número de intentos según la dificultad elegida."""
    level = input("Elige una dificultad: escribe 'easy' o 'hard': ").lower()
    
    if level == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def game():
    print("🎯 Bienvenido al juego de Adivina el Número")
    print("Estoy pensando en un número entre 1 y 100.")
    secret_number = random.randint(1, 100)
    
    attempts = set_difficulty()

    guess = 0
    while guess != secret_number and attempts > 0:
        print(f"Te quedan {attempts} intentos.")
        guess = int(input("Adivina un número: "))
        
        attempts = check_guess(guess, secret_number, attempts)

        if guess == secret_number:
            break
        elif attempts == 0:
            print(f"Te quedaste sin intentos. El número correcto era {secret_number}")

game()