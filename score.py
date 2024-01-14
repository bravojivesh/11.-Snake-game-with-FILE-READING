from turtle import Turtle

ALIGNMENT= "center"
FONT= ("arial", 25, "normal") #the self write syntax takes a tuple. So instead of creating 3 separate
# variables, we can just create one tuple.

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.hideturtle()
        self.goto(0,290)
        self.write(f"Score:{self.count} ", False, align=ALIGNMENT, font=FONT)

        # self.write((0,0), True)

    def update(self):
        self.count += 1
        self.clear()
        self.write(f"Score:{self.count} ", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)





