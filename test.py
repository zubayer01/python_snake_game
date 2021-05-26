from turtle import Screen
from sanke import Snake
from food import Food
from scoreboard import ScoreCount
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenxia")
screen.tracer(0)

snake = Snake()
food = Food()
scoreShow = ScoreCount()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameCondition = True
score = 0
while gameCondition:
    screen.update()
    time.sleep(0.1)
    snake.move(20)

    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        scoreShow.game_over()
        gameCondition = False

    if snake.snake[0].distance(food) < 15:
        food.refresh()
        score += 1
        scoreShow.count(score)
        snake.snake_bite()

    for i in range(1, len(snake.snake)):
        if snake.snake[0].distance(snake.snake[i]) < 10:
            scoreShow.game_over()
            gameCondition = False

screen.exitonclick()
