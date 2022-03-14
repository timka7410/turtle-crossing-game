from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 260)
        self.write("Level: ", True, align="center", font=FONT)
        self.write(self.level, align="center", font=FONT)

    def new_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.color("black")
        self.goto(00, 0)
        self.write("GAME OVER", True, align="center", font=("Courier", 28, "bold"))