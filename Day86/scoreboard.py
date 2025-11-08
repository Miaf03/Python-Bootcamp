from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 260)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 18, "bold"))
        self.goto(250, 260)
        self.write(f"Lives: {self.lives}", align="left", font=("Courier", 18, "bold"))

    def add_point(self):
        self.score += 10
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 26, "bold"))

    def you_win(self):
        self.goto(0, 0)
        self.color("lime")
        self.write("YOU WIN!", align="center", font=("Courier", 26, "bold"))