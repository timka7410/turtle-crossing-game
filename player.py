from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.pen()
        self.seth(90)
        self.color("black")
        self.shape("turtle")


    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.fd(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.penup()
        self.seth(90)


