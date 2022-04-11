from turtle import Turtle, Screen


class Player:
    def __init__(self):
        self.T = []
        self.create()
        self.player = self.T[0]

    def create(self):
        t = Turtle()
        t.speed(0)
        t.penup()
        t.goto(-450, 0)
        t.color("white")
        t.shape("square")
        t.shapesize(stretch_wid=4, stretch_len=0.7)
        t.speed(0)
        self.T.append(t)
        self.posY = 0

    def up(self):
        self.posY += 30
        self.player.goto(-450, self.posY)

    def down(self):
        self.posY -= 30
        self.player.goto(-450, self.posY)
