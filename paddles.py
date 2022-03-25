from turtle import Turtle



# Class for making the paddle.
class Paddle(Turtle):
    def __init__(self, position:tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.penup()
        self.goto(position)


# Functions for making the paddle move up and down.
    def go_up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 50 
        self.goto(self.xcor(), new_y)







