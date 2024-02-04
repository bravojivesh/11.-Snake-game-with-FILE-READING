from turtle import Turtle

ALIGNMENT= "center"
FONT= ("arial", 25, "normal") #the self write syntax takes a tuple. So instead of creating 3 separate
# variables, we can just create one tuple.

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Score.txt", mode="r") as file:
            self.highscore= int(file.read()) #reads the data from the score.txt and changes to int for conversion later
        self.penup()
        self.hideturtle()
        self.goto(-80,290)
        self.write(f"Score:{self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)


        # self.write((0,0), True)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore} ", False, align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.score > self.highscore:
            self.highscore=self.score
            self.score=0
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore} ", False, align=ALIGNMENT, font=FONT)
        with open ("Score.txt", mode="w") as score_file:
            score_file.write(f"{self.highscore}") #when higher write to this file.

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)





