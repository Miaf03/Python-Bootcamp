import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

# Define colors and turtles list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# Ask for the user's bet
user_bet = screen.textinput("Make your bet", f"Which turtle will win the race? Choose from: {', '.join(colors)}").lower()

# Create and position the turtles
start_y = -100
for index, color in enumerate(colors):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y + index * 40)
    turtles.append(new_turtle)

# Start the race
winner_color = None
race_on = True if user_bet in colors else False

while race_on:
    for racer in turtles:
        distance = random.randint(1, 10)
        racer.forward(distance)

        if racer.xcor() >= 230:
            winner_color = racer.pencolor()
            race_on = False
            break

# Announce the result
if winner_color == user_bet:
    print(f"You've won! The {winner_color} turtle is the winner!")
else:
    print(f"You've lost. The {winner_color} turtle won the race.")

# Keep the window open
screen.exitonclick()