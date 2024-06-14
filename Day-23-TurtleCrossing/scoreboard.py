FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update()
        
    def level_up(self):
        self.level += 1
        self.update()
        
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over!", align = "center", font = FONT)

