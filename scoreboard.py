from turtle import Turtle, Screen
FONT = ("Arial", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
    
        
    
    def update_scoreboard(self):
        self.write(f"{self.score}", align ="center", font = FONT)
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
        
       

    










# r_paddle = Turtle()
# r_paddle.color('white')
# r_paddle.hideturtle()
# r_paddle.penup()
# r_paddle.goto(100,240)
# r_paddle.write(arg = f"{score_r_paddle}", align = "center", font = FONT)



        
    # def __init__(self):
    #     super().__init__()
    #     self.score = 0
    #     self.color("white")
    #     self.penup()
    #     self.goto(0, 270)
    #     self.hideturtle()
    #     self.update_scoreboard()

    # def update_scoreboard(self):
    #     self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # def increase_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_scoreboard()

