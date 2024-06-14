from turtle import Screen
import time
from snake import *
from food import *
from score import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_running = True

while game_running:
    screen.update()
    time.sleep(0.08)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 20:
        food.remake()
        score.score += 1
        score.show_score()
        snake.extend()
        
    #Detect collision
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.game_over()
        game_running = False
        
    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            game_running = False
            score.game_over()


screen.exitonclick()