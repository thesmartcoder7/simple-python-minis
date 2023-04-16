from turtle import Turtle


class WriteState(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.single_state = state
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x, y)

    def update_map(self):
        self.write(f"{self.single_state}", align="center", font=('arial', 8, 'normal'))
