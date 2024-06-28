from turtle import Turtle

Font=("Arial",24,"normal")

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_lives=6
        self.hideturtle()
        self.penup()
        self.color("red")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"score:{self.l_score}",align="left",font=Font)
        self.goto(200,250)
        self.write(f"lives:{self.r_lives}",align="left",font=Font)


    def increase_score(self):
        self.l_score+=1
        self.clear()
        self.update_score()

    def decrease_level(self):
        self.r_lives-=1
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAMEOVER",align="left",font=Font)


    
   

        
        