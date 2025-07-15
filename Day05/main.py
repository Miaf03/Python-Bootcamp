# Password Generator:
# Ask the user how many letters, symbols, and numbers they want in their password

import random

print("\nWelcome to the PyPassword Generator!\n")

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

password = []

for _ in range(num_letters):
    password.append(random.choice(letters))

for _ in range(num_symbols):
    password.append(random.choice(symbols))

for _ in range(num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

final_password = "".join(password)
print(f"Your generated password is: {final_password}")