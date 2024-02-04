import turtle as tu

x_cord = 0
y_cord = 0

positions = [(x_cord, y_cord), (x_cord - 20, y_cord), (x_cord - 40, y_cord)]

class Biggie:

    def __init__(self):
        self.biggie_list = []
        self.first_segments()
    def create_biggie(self, location): #this will be used only in this module. To create new segments.
        # in the background
        biggie = tu.Turtle()
        biggie.shape("square")
        biggie.color("white")
        biggie.penup()
        biggie.goto(location)
        self.biggie_list.append(biggie)

    def first_segments(self): #dont need to call this separately. It will be a part of class invocation.
        for i in range (len(positions)):
            self.create_biggie(positions[i])

    def move_big_mackie(self):
            for b in range(len(self.biggie_list) - 1, 0, -1):
                new_x = self.biggie_list[b - 1].xcor()  # grabbing the x-cordinate of the piece that is one step before. When b is the last one, this will be for one step ahead of b.
                new_y = self.biggie_list[b - 1].ycor()  # grabbing the y-cordinate of the piece that is one step before.
                self.biggie_list[b].goto(new_x, new_y)  # telling that last piece to go to "the position that is one step ahead"
            self.biggie_list[0].forward(20)


    def add_tail(self):
        x_cord1= self.biggie_list[-1].xcor()
        y_cord1=self.biggie_list[-1].ycor()
        location1= (x_cord1, y_cord1)
        self.create_biggie(location=location1)

    def reset(self):
        for member in self.biggie_list:
            member.goto(999,999)
        self.biggie_list.clear()
        self.first_segments()

    def move_up(self):
        direction= self.biggie_list[0].heading()
        if direction == 0:
            self.biggie_list[0].left(90)
        elif direction==180:
            self.biggie_list[0].right(90)

    def move_down(self):
        direction= self.biggie_list[0].heading()
        if direction == 0:
            self.biggie_list[0].right(90)
        elif direction==180:
            self.biggie_list[0].left(90)

    def move_left(self): #when a straight line horizontally, left and right should not work. So no need
        # to handle those.
        direction= self.biggie_list[0].heading()
        # if direction == 0:
        #     self.biggie_list[0].left(-180)
        if direction==90:
            self.biggie_list[0].left(90)
        elif direction==270:
            self.biggie_list[0].right(90)

    def move_right(self): #when a straight line horizontally, left and right should not work. So no
        # need to handle those.
        direction= self.biggie_list[0].heading()
        if direction==90:
            self.biggie_list[0].right(90)
        elif direction==270:
            self.biggie_list[0].left(90)