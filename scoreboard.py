from turtle import Turtle

ALIGN = "left"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_scoreboard(pos)
        
    def create_scoreboard(self, pos):
        self.score = 0
        self.up()
        self.x = pos
        self.setpos(self.x, 250)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.score}", True, ALIGN, FONT)
    
    def add_score(self):
        self.clear()
        self.score +=1
        self.setpos(self.x, 250)
        self.write(f"{self.score}", True, ALIGN, FONT)