from turtle import Turtle

WIDTH = 1
HEIGHT = 5
XPOS = [350, -350]
YPOS = 0
MOVE = 20

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.createPaddle(pos)
    
    def createPaddle(self, pos):
        self.shape("square")
        self.shapesize(stretch_len=WIDTH, stretch_wid=HEIGHT)
        self.up()
        self.color("white")
        self.setpos(XPOS[pos], YPOS)

    def moveUp(self):
        ycor = self.ycor()
        self.sety(ycor+MOVE)
    
    def moveDown(self):
        ycor = self.ycor()
        self.sety(ycor-MOVE)