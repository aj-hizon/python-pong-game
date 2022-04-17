from turtle import Turtle


# Class for making the Ball.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.penup()
        self.x_move = 0.70
        self.y_move = 0.70

# Method for making the ball move.
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
# Method for having to bounce from y axis.
    def bounce_y(self):
        self.y_move *= -1 
    
# Method for having to bounce from x axis.
    def bounce_x(self):
        self.x_move *= -1
 
# Method for resetting where the ball goes
    def reset_ball(self):
        self.goto(0, 0)

        
       


