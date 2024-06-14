import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move()
    screen.update()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.gameover()
            game_is_on = False
    
    if player.finish():
        player.start_line()
        car_manager.speed_up()
        scoreboard.level_up()
        
        
    
screen.exitonclick()