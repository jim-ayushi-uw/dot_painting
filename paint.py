import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(213, 157, 89), (238, 214, 95), (34, 106, 151), (126, 168, 198), (152, 76, 54), (208, 134, 163), (211, 85, 62), (155, 61, 82), (22, 39, 54), (173, 161, 49), (200, 87, 121), (136, 183, 151), (57, 117, 91), (228, 168, 187), (240, 212, 5), (27, 47, 38), (88, 156, 99), (66, 47, 34), (38, 165, 188), (227, 175, 166), (10, 98, 75)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()