# Treasure Island

# - You're at a crossroad. Where do you want to go? 'left' or 'right'
# - If you choose left, you arrive at a lake. If you choose right, you fall into a hole
# - If you type 'wait', you wait for a boat. If you type 'swim', you cross swimming and get attacked by a trout
# - If you waited, you arrive at the island safely and find a house with 3 doors: red, yellow, and blue. Choose one
# - The red door is a room full of fire, the yellow door is where the treasure is, and the blue door is full of crocodiles

print("\nWelcome to Treasure Island!")
print("Your mission is to find the treasure.\n") 

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right':\n").lower()

if choice1 == "left":
    print("You've come to a big, deep lake.")

    choice2 = input("\nDo you want to wait for a boat? Type 'wait' or 'swim' to cross:\n").lower()

    if choice2 == "wait":
        print("You've arrived at the island safely.")

        choice3 = input("\nYou find a house with 3 doors: 'red', 'yellow', and 'blue'. Which one do you choose?\n").lower()

        if choice3 == "red":
            print("You've entered a room full of fire! Game Over!")

        elif choice3 == "yellow":
            print("You've found the treasure! Congratulations, you won!")

        elif choice3 == "blue":
            print("You've entered a room full of crocodiles! Game Over!")

        else:
            print("You can only choose one of the following options: 'red', 'yellow', or 'blue'")

    elif choice2 == "swim":
        print("You've been bitten by a trout! Game Over!")

    else:
        print("You can only type 'wait' or 'swim'")

elif choice1 == "right":
    print("You've fallen into a hole! Game Over!")

else:
    print("You can only choose 'left' or 'right'")