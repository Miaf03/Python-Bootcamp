# Cifrado César:

# Programa para cifrar y descifrar mensajes usando el cifrado César
# El usuario elige si quiere cifrar o descifrar
# Se ignoran los símbolos, espacios o números (no se modifican)
# Se puede ejecutar el programa varias veces seguidas

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    
  end_text = ""
  
  if cipher_direction == "decode":
    shift_amount *= -1
    
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
      
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

run = True

while run:
      
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
  
  if choice == 'no':
    run = False

    print("Goodbye.")