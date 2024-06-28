from turtle import Screen
import time
from paddle import Paddle
from ball import RainBall
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("rain ball")
screen.tracer(0)


paddle=Paddle((0,-270))
ball=RainBall()
scoreboard=Score()


screen.listen()
screen.onkey(paddle.go_right,"Right")
screen.onkey(paddle.go_left,"Left")



game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
   

    ball.create_ball()
    ball.move_ball()

    for s in ball.all_balls:
        if s.distance(paddle)<20:
            scoreboard.increase_score()
            ball.remove(s)

        if s.ycor() <-290:
            ball.remove(s)
            scoreboard.decrease_level()
            if scoreboard.r_lives ==0:
                game_is_on=False
                scoreboard.gameover()



screen.exitonclick()