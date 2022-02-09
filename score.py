from turtle import Turtle
ALIGNMENT='center'
FONT=font=('Courier', 22, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def inc_score(self):
        self.score=self.score+1
        self.clear()
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)