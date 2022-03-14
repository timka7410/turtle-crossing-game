import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.exitonclick()

    if player.ycor() > 275:
        scoreboard.new_level()
        player.reset_position()
        car_manager.speed_up()

