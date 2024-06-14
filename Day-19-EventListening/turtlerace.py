from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400)
y = -125
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for turtle_no in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_no])
    new_turtle.penup()
    new_turtle.setpos(x=-230, y = y)
    y+=50
    turtles.append(new_turtle)

race = False
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
if bet:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race = False
            if bet == winner:
                print(f"You Win! The winner was {winner}.")
            else:
                print(f"You lose... The winner was {winner}.")
            break
        pace_distance = random.randint(0,10)
        turtle.forward(pace_distance)
    
    
screen.exitonclick()