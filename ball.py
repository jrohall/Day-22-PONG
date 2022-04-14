from turtle import Turtle
import random


class Ball:
    def __init__(self):
        self.ballList = []
        self.createBall()
        self.ball = self.ballList[0]

    def createBall(self):
        b = Turtle()
        b.speed(0)
        #b.shape("circle")
        b.color("red")
        b.penup()
        self.ballY = 0
        self.ballX = 0
        b.goto(self.ballX, self.ballY)
        b.shapesize(stretch_wid=2, stretch_len=2)
        self.ballList.append(b)

    def ballMove(self):
        self.ballHeading = self.ball.heading()
        newHeading = random.randint(0, 360)
        self.ball.setheading(newHeading)
        self.ballBounce()
    def ballBounce(self):
        gameIsOn = True
        while gameIsOn:
            if self.ball.xcor() > -450 and self.ball.xcor() < 450 and self.ball.ycor() > -350 and self.ball.ycor() < 350:
                self.ball.forward(8)
            elif self.ball.xcor() >= 450 or self.ball.xcor() <= -450:
                ang1 = self.ball.heading() - 315
                self.ball.setheading(ang1)
                self.ball.forward(8)
            elif self.ball.ycor() >= 350 and self.ball.heading()<0:
                 ang2a = self.ball.heading() - 45
                 self.ball.setheading(ang2a)
                 self.ball.forward(8)
            elif self.ball.ycor() >= 350 and self.ball.heading()>90:
                 ang2b = self.ball.heading() + 45
                 self.ball.setheading(ang2b)
                 self.ball.forward(8)
            elif self.ball.ycor() >= 350 and self.ball.heading()>0:
                 ang2b = self.ball.heading() + 315
                 self.ball.setheading(ang2b)
                 self.ball.forward(8)
            elif self.ball.ycor() <= -350:
                ang3 = self.ball.heading() + 45
                self.ball.setheading(ang3)
                self.ball.forward(8)
            else:
                pass
 
#            elif self.ball.ycor() >= 350 and self.ball.heading() < 90 and self.ball.heading() > 0:
#                newTopAngle = self.ball.heading() + 45
#                self.ball.setheading(newTopAngle)
#                self.ball.forward(8)
# The ball works, but I am having trouble really grasping how to make the ball bounce to where it makes sense, sometimes it turns odd angles, other times it just doesn't look right.
