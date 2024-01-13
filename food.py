import random
import turtle

class Food(turtle.Turtle): #this has to be class not a module
        def __init__(self):
            super().__init__()
            self.color("blue")
            self.shape("circle")
            self.shapesize(stretch_len=0.8, stretch_wid=0.8)

        def create_food(self):
            rand_x= random.randint(-270,270)
            rand_y= random.randint(-270,270)
            self.penup()
            self.goto(rand_x,rand_y)




