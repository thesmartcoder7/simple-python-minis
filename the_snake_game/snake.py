from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        segment = Turtle(shape="square")
        segment.shapesize(stretch_wid=0.7, stretch_len=0.7)
        segment.speed(0)
        segment.penup()
        segment.goto(position)
        segment.color("white")
        self.snake_body.append(segment)

    def extend(self):
        self.create_segment(self.snake_body[-1].position())

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        heading = self.head.heading()
        if heading == 0:
            heading += 90
            self.head.setheading(heading)
        elif heading == 180:
            heading -= 90
            self.head.setheading(heading)
        else:
            return

    def down(self):
        heading = self.head.heading()
        if heading == 0:
            heading -= 90
            self.head.setheading(heading)
        elif heading == 180:
            heading += 90
            self.head.setheading(heading)
        else:
            return

    def right(self):
        heading = self.head.heading()
        if heading == 90:
            heading -= 90
            self.head.setheading(heading)
        elif heading == 270:
            heading += 90
            self.head.setheading(heading)
        else:
            return

    def left(self):
        heading = self.head.heading()
        if heading == 90:
            heading += 90
            self.head.setheading(heading)
        elif heading == 270:
            heading -= 90
            self.head.setheading(heading)
        else:
            return
