from turtle import Turtle
import random

colors=["blue","yellow","pink","purple","red","green"]
start_move_distance=5
move_increment=10


class RainBall:
    def __init__(self):
        self.all_balls=[]
        self.ball_speed=start_move_distance
       


    def create_ball(self):
        random_chance=random.randint(1,20)
        if random_chance ==1:
            new_ball =Turtle("circle")
            new_ball.shapesize(1,1)
            new_ball.penup()
            new_ball.setheading(270)
            new_ball.color(random.choice(colors))
            random_x=random.randint(-270,270)
            new_ball.goto(random_x,300)
            self.all_balls.append(new_ball)
            

    def move_ball(self):
        for ball in self.all_balls:
            ball.forward(10)

    def remove(self,obj):
        self.all_balls.remove(obj)
        obj.hideturtle()

    