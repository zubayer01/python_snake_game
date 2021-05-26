from turtle import Turtle


class ScoreCount(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.score = 0
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 12, 'normal'))
        self.hideturtle()

    def count(self, num):
        self.score = num
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 12, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align="center", font=('Arial', 30, 'normal'))
        self.hideturtle()
