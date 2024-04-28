from turtle import Turtle

class Scroboard(Turtle):

    ALLIGNMENT ="center"
    FONT = ("Arial",24, "normal")

    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=self.ALLIGNMENT, font=self.FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=self.ALLIGNMENT, font=self.FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()