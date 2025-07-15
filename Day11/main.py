'''Día 11. Blackjack:

- Se reparten 2 cartas al usuario y 2 cartas a la computadora.
- Se calcula la puntuación de cada uno, contando el As como 11 o 1 según convenga.
- El usuario puede pedir más cartas o plantarse.
- La computadora roba cartas hasta alcanzar al menos 17 puntos.
- Se comparan las puntuaciones y se muestra el resultado final (ganar, perder o empate).
- Al final se pregunta si se quiere jugar otra vez y se limpia la consola.'''

import os
import random
from art import logo

def clear_console():
    """Limpia la consola para un nuevo juego"""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Devuelve una carta aleatoria del mazo"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """Calcula el puntaje actual de una mano"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare_scores(user_score, computer_score):
    """Devuelve el resultado del juego comparando los puntajes"""
    if user_score == computer_score:
        return "Empate"
    elif computer_score == 0:
        return "¡Perdiste! El oponente tiene Blackjack 🃏"
    elif user_score == 0:
        return "¡Ganaste con Blackjack!"
    elif user_score > 21:
        return "Te pasaste de 21. Pierdes"
    elif computer_score > 21:
        return "El oponente se pasó de 21. ¡Ganas!"
    elif user_score > computer_score:
        return "¡Ganaste!"
    else:
        return "Perdiste"

def play_game():
    clear_console()
    print(logo)

    user_hand = []
    computer_hand = []

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"\nTus cartas: {user_hand}, puntuación actual: {user_score}")
        print(f"Primera carta del computador: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("¿Quieres otra carta? Escribe 's' para sí o 'n' para no: ").lower()
            while choice not in ['s', 'n']:
                choice = input("Por favor, escribe 's' para sí o 'n' para no: ").lower()

            if choice == 's':
                user_hand.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_hand) != 0 and calculate_score(computer_hand) < 17:
        computer_hand.append(deal_card())

    computer_score = calculate_score(computer_hand)
    user_score = calculate_score(user_hand)

    print(f"\nTu mano final: {user_hand}, Puntuación final: {user_score}")
    print(f"Mano final del computador: {computer_hand}, Puntuación final: {computer_score}")
    print(compare_scores(user_score, computer_score))

while True:
    play_again = input("\n¿Quieres jugar una partida de Blackjack? Escribe 's' o 'n': ").lower()
    while play_again not in ['s', 'n']:
        play_again = input("Por favor, escribe 's' para sí o 'n' para no: ").lower()
    
    if play_again == 's':
        play_game()
    else:
        print("¡Gracias por jugar! 👋")
        break