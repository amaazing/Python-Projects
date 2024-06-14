from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape(name="blank")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y= 270)
        self.score = 0
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial",20,"normal"))
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over!", move=False, align="center", font=("Arial",20,"normal"))
        
        