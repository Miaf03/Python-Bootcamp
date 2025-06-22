'''Día 9. Subasta secreta:

- Varios usuarios ingresan su nombre y su oferta.
- Cada oferta es secreta (se limpia la pantalla entre turnos).
- Se guardan los datos en un diccionario: clave = nombre, valor = oferta.
- Al final, se determina quién hizo la oferta más alta y se anuncia al ganador.'''

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the secret auction program.")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}

while True:
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if should_continue != "yes":
        break
    else:
        clear()
        
find_highest_bidder(bids)


# Notas:

# import os
# os.system('cls' if os.name == 'nt' else 'clear')

# Estamos importando el módulo 0S que permite interactuar con el sistema operativo 
# Si estás en Windows ejecuta cls. Si estás en Linux/Mac ejecuta clear. Ambos comandos borran la pantalla de la terminal
