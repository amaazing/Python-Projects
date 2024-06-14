COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

        
    def create_cars(self):
        if random.randint(1,6) == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(1, 2)
            car.penup()
            car.goto(300 ,random.randint(-250, 250))
            self.all_cars.append(car)
        
    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)
            
    def speed_up(self):
        self.speed += MOVE_INCREMENT
            
    