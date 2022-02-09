from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.inc_score()

    
    if snake.segments[0].xcor()>300 or snake.segments[0].xcor()<-300 or snake.segments[0].ycor()>300 or snake.segments[0].ycor()<-300:
        game_is_on=False
        score.game_over()

    for i in range(1,len(snake.segments),1):
        if snake.segments[i].distance(snake.segments[0]) <10:
            game_is_on=False
            score.game_over()

   
    
    
    










screen.exitonclick()