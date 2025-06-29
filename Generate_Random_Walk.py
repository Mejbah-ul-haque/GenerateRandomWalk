import turtle as t
import random

tim = t.Turtle()

directions =[0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast") #fast, fastest, normal, slow, slowest

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))