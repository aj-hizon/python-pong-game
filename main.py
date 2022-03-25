from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from design import Design
import time


title_of_game = Design(text = "THE PONG GAME", font_size = 15, position = (0, -270))
author = Design(text = "-- BY PROKU --", font_size = 7, position = (0, -280))


game_is_on = True 


# Making the screen.
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.title("Proku's Pong Game")


# Making the paddle objects.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# Making the ball object. 
ball = Ball()


# Making the objects for the scoreboard
r_paddle_score = Scoreboard(position = (200, 240))
l_paddle_score = Scoreboard(position = (-200, 240))


# Keybindings (calling the function using self.function-name)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


r_paddle_score = Scoreboard(position = (100, 240))
l_paddle_score = Scoreboard(position = (-100, 240))


while game_is_on:
    screen.update() 
    ball.move()
   
    
  
   
# Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()


# Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    

# Detect when paddle misses
    if ball.xcor() > 390: 
        # add points to the l_paddle_score
        l_paddle_score.increase_score()
        ball.reset_ball()
       

    if ball.xcor() < -390:
        # add points to the r_paddle_score
        r_paddle_score.increase_score()
        ball.reset_ball()
        # add points






