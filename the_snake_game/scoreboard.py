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
        with open("data.txt", mode="r") as data:
            data_score = data.read()
        self.high_score = int(data_score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"#Score: {self.count} #High_Score: {self.high_score}", align=alignment, font=font)

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
        with open("data.txt", mode="w") as data_new:
            data_new.write(str(self.high_score))
        self.count = 0
        self.update_scoreboard()

    def game_over(self):
        self.write("Continue? Y or N?", align=alignment, font=font)

    def increase_score(self):
        self.count += 10
        self.update_scoreboard()
