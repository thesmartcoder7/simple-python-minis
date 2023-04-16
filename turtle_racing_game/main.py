from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700, height=600)
colors = ["red", "orange", "indigo", "green", "blue", "purple"]
all_turtles = []
y_positions = [-160, -100, -40, 20, 80, 140]

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle do you think will win the race?")

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_positions[turtles])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print("Congratulations! your turtle has won the race!!! ")
            else:
                print(f"Sorry, your turtle was not faster than the {turtle.pencolor()} turtle.")
                print("You have lost the bet!")
        else:
            distance = random.randint(0, 10)
            turtle.forward(distance)

screen.exitonclick()
