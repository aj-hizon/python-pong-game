from turtle import Turtle, Screen
FONT = ("Arial", 15, "bold")

class Design(Turtle):
    """Class for putting the title and author."""
    def __init__(self, text, font_size, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(arg = text, align = "center", font = ("Arial", font_size, "bold"))