'''
Day 22: Pong
Author: Maaz Ali
Date: May 17 2024
A program to play pong.
'''
from turtle import Screen
from paddle import Paddle
from puck import Puck
from score import Score

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
puck = Puck()
score = Score()




game_on = True
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
while game_on:
    time.sleep(puck.move_speed)
    screen.update()
    puck.move()
    
    if puck.ycor() > 280 or puck.ycor() < -280:
        puck.bounce_y()
        
    #Collision with paddles
    if (puck.distance(r_paddle) <  50 and puck.xcor() > 320) or (puck.distance(l_paddle) < 50 and puck.xcor() < -320):
        puck.bounce_x()
        
    if puck.xcor() > 390:
        puck.reset_pos()
        score.rightpoint()
        screen.update()
        time.sleep(1)
        
    if puck.xcor() < -390:
        puck.reset_pos()
        score.leftpoint()
        screen.update()
        time.sleep(1)
    
screen.exitonclick()