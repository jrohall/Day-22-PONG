from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddleList = []
        self.createPaddle()
        self.paddle = self.paddleList[0]

    def createPaddle(self):
        padd = Turtle()
        padd.speed(0)
        padd.penup()
        padd.goto(450, 0)
        padd.color("white")
        padd.shape("square")
        padd.shapesize(stretch_wid=4, stretch_len=0.7)
        padd.speed(0)
        self.paddleList.append(padd)
        self.paddY = 0

    def moveUp(self):
        self.paddY += 1.5
        self.paddle.goto(450, self.paddY)

    def moveDown(self):
        self.paddY -= 1.5
        self.paddle.goto(450, self.paddY)