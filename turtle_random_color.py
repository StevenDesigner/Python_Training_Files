import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    random_rgb=(r,g,b)
    return random_rgb

    
########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
