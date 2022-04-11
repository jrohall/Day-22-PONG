# body of the Pong game
from turtle import Screen, Turtle
from player import Player
from paddle import Paddle
from ball import Ball
import time

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("PONG")

# background lines
lineY = -400
for w in range(8):
    line = Turtle()
    line.color("black")
    line.speed(0)
    line.shape("square")
    line.penup()
    line.goto(0, lineY)
    line.shapesize(stretch_wid=2, stretch_len=0.5)
    lineY += 100
    line.color("white")

# objects
ball = Ball()
player = Player()
paddle = Paddle()

# listens to executable keys for controlling the player
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.listen()

# ball movement
ball.ballMove()

# constant movement for the computer paddle
gameOn = True
while paddle.paddY <= 310:
    paddle.moveUp()
while gameOn:
    for n in range(400):
        paddle.moveDown()
    for i in range(400):
        paddle.moveUp()

screen.exitonclick()
