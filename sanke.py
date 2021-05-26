from turtle import Turtle


class Snake:
    def __init__(self, snakes=3):
        self.snakes = snakes
        self.snake = []
        self.createSnake(self.snakes)

    def createSnake(self, num):
        posX = 0
        for i in range(num):
            part = Turtle()
            part.shape('square')
            part.color('white')
            part.penup()
            part.goto(x=posX, y=0)
            posX -= 20
            self.snake.append(part)

    def move(self, num):
        for i in range(len(self.snake) - 1, 0, -1):
            ordX = self.snake[i - 1].xcor()
            ordY = self.snake[i - 1].ycor()
            self.snake[i].goto(x=ordX, y=ordY)
        self.snake[0].forward(num)

    def snake_bite(self):
        part = Turtle()
        part.shape('square')
        part.color('white')
        part.penup()
        ordX = self.snake[-1].xcor()
        ordY = self.snake[-1].ycor()
        part.goto(x=ordX, y=ordY)
        self.snake.append(part)

    def up(self):
        state = self.snake[0].heading()
        if state == 0 or state == 180:
            self.snake[0].setheading(90)

    def down(self):
        state = self.snake[0].heading()
        if state != 90:
            self.snake[0].setheading(270)

    def left(self):
        state = self.snake[0].heading()
        if state != 0:
            self.snake[0].setheading(180)

    def right(self):
        state = self.snake[0].heading()
        if state != 180:
            self.snake[0].setheading(0)
