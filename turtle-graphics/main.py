import turtle as t
import random


turtle = t.Turtle()
turtle.pensize(1)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


def shapes():
    for sides in range(3, 50):
        turtle.pencolor(random_color())
        for _ in range(sides):
            angle = 360 / sides
            turtle.right(angle)
            turtle.forward(20)


def random_walk():
    moves = ["right", "left", "forward", "backward"]
    turtle.speed(0)
    for _ in range(1, 500):
        move = random.choice(moves)
        turtle.pencolor(random_color())
        if move == "right":
            turtle.right(90)
            turtle.forward(20)
        elif move == "left":
            turtle.left(90)
            turtle.forward(20)
        elif move == "forward":
            turtle.forward(20)
        else:
            turtle.backward(20)


def spirograph():
    turtle.speed(0)
    angle = 0
    for _ in range(0, 361):
        turtle.color(random_color())
        turtle.circle(100, extent=None, steps=None)
        turtle.right(angle)
        angle += 1


# shapes()
# random_walk()
spirograph()
screen = t.Screen()
screen.exitonclick()
