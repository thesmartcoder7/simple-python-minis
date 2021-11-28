from turtle import Turtle

alignment = "center"
font = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.count = 0

    def update_scoreboard(self):
        self.write(f"Score: {self.count}", align=alignment, font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!", align=alignment, font=font)

    def increase_score(self):
        self.count += 10
        self.clear()
        self.update_scoreboard()
