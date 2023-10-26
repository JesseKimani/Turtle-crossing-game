import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            car_manager.game_over()
    if player.ycor() > 290:
        player.refresh()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
