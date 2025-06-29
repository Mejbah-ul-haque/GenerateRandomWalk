import turtle as t
import random

tim = t.Turtle()

colors = ["chartreuse", "red", "IndianRed", "blue", "orange", "purple", "pink", "green", "seaGreen"]
directions =[0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast") #fast, fastest, normal, slow, slowest

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))