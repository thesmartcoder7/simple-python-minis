import random
import turtle as t

colors_list = [(34, 108, 167), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94),
               (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152),
               (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0),
               (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203),
               (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46),
               (99, 93, 2), (43, 151, 190), (10, 111, 51), (228, 169, 182), (177, 186, 217)]

t.colormode(255)
turtle = t.Turtle()
turtle.speed(0.5)
turtle.penup()
turtle.setx(-200)
set_y = -200
turtle.hideturtle()

for _ in range(10):
    turtle.sety(set_y)
    for _ in range(10):
        turtle.sety(set_y)
        turtle.pencolor(random.choice(colors_list))
        turtle.pendown()
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)

    turtle.setx(-200)
    set_y += 50

screen = t.Screen()
screen.exitonclick()
