'''Día 7. Hangman:

- Juego clásico donde el usuario debe adivinar una palabra letra por letra.
- El usuario tiene una cantidad limitada de intentos antes de perder.
- Si adivina una letra correcta, se muestra en su posición dentro de la palabra.
- Si se equivoca, pierde una vida.
- El juego termina si adivina toda la palabra o se queda sin vidas.'''

import random

from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

end_of_game = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")

    if not "_" in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])