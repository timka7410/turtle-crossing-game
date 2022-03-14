from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_car = []
        self.speed = 5

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.x = 300
            new_car.y = random.randint(-250, 250)
            new_car.goto(new_car.x,new_car.y)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            self.all_car.append(new_car)

    def speed_up(self):
        if self.speed >= 5:
            self.speed += MOVE_INCREMENT


    def move_cars(self):

        for car in self.all_car:
            car.backward(self.speed)

