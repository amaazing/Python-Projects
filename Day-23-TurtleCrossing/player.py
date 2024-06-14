STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.start_line()
        self.setheading(90)
        
    def move(self):
        self.goto(0 , self.ycor() + MOVE_DISTANCE)
        
    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else: 
            return False
    
    def start_line(self):
        self.goto(STARTING_POSITION)
        

        