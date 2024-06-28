from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(90)


    def go_right(self):
       if not (self.xcor()>250):
            new_x=self.xcor()+20
            self.goto(new_x,self.ycor())


    
    def go_left(self):
        if not (self.xcor()<-250):
            new_x=self.xcor()-20
            self.goto(new_x,self.ycor())

    
    
