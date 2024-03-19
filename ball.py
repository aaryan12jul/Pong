from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
    
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        self.setpos(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self, contact):
        if contact == "x":
            self.x_move *= -1
        elif contact == "y":
            self.y_move *= -1
    
    def speed(self):
        if self.x_move > 0:
            self.x_move += 1
        elif self.x_move < 0:
            self.x_move -= 1
        
        if self.y_move > 0:
            self.y_move += 1
        elif self.y_move < 0:
            self.y_move -= 1
    
    def reset(self):
        self.setpos(0,0)
        
        if self.x_move > 0:
            self.x_move = 10
        elif self.x_move < 0:
            self.x_move = -10
        
        if self.y_move > 0:
            self.y_move = 10
        elif self.y_move < 0:
            self.y_move = -10

        self.bounce("x")