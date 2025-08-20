# Rock, Paper, Scissors:

# * 0 = rock
# * 1 = paper
# * 2 = scissors
# - The computer chooses randomly

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
computer_choice = random.randint(0, 2)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

print(f"\nComputer chose:\n{options[computer_choice]}")
print(f"\nYou chose:\n{options[user_choice]}")

if computer_choice == user_choice:
    print("It's a draw!")
elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
    print("Computer wins!")
else:
    print("You win!")