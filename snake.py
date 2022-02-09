from turtle import Turtle
MOVE_DISTANCE=20
UP = 90
DOWN=270
LEFT=180
RIGHT=0
position=[(-20,0),(-40,0),(-60,0)]
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
    
    def create_snake(self):
        for pos in position:
            self.add_segment(pos)
           
    
    def move(self):
         for seg_num in range(len(self.segments)-1,0,-1):
             new_x=self.segments[seg_num-1].xcor()
             new_y=self.segments[seg_num-1].ycor()
             self.segments[seg_num].goto(new_x,new_y)
         self.segments[0].forward(MOVE_DISTANCE)
    
    def add_segment(self,pos):
            tim= Turtle(shape='square')
            tim.color('white')
            tim.penup()
            tim.goto(pos)
            self.segments.append(tim)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    
    
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
           self.segments[0].setheading(RIGHT)