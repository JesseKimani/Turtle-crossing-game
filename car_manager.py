from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.penup()
        self.hideturtle()
        self.car_speed = 0.1

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_y = random.randint(-220, 220)
            new_car.goto(300, new_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def game_over(self):
        self.write("GAME OVER!", align="center", font=('Courier', 24, 'normal'))

    def increase_speed(self):
        self.car_speed *= 0.7
