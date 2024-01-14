import turtle as tu

x_cord = 0
y_cord = 0

positions = [(x_cord, y_cord), (x_cord - 20, y_cord), (x_cord - 40, y_cord)]


class Biggie:

    def __init__(self):
        self.biggie_list = []
        self.create_biggie() #this is why it was creating 6 instances instead of 3. I do not need to call this method here.
        # It is calling the method right when it is creating a Biggie object.

    def create_biggie(self):
        for i in range(len(positions)):  # Iterate three times
            biggie = tu.Turtle()
            biggie.shape("square")
            biggie.color("white")
            biggie.penup()
            biggie.goto(positions[i])
            self.biggie_list.append(biggie)
            # print(len(self.biggie_list), self.biggie_list)
            # print(biggie.xcor(), biggie.ycor())



    def move_big_mackie(self):
            for b in range(len(self.biggie_list) - 1, 0, -1):  # we want to start from the end and move each piece one step ahead.
                # So this means: it will return only an INTEGER. And the stop value is NOT INCLUSIVE. So if length is 3,
                # then only 2 and 1.
                # the first piece is NOT in the loop. We have to mention it outside of the loop to move it one step ahead.
                # print(b)
                new_x = self.biggie_list[b - 1].xcor()  # grabbing the x-cordinate of the piece that is one step before. When b is the last one, this will be for one step ahead of b.
                new_y = self.biggie_list[b - 1].ycor()  # grabbing the y-cordinate of the piece that is one step before.
                self.biggie_list[b].goto(new_x, new_y)  # telling that last piece to go to "the position that is one step ahead"
            self.biggie_list[0].forward(20)

#angela has done the following differently. Example below for turning right:
    # define a constant like LEFT
    # if list[0].heading != LEFT:
    #       list[0].setheading (180)
    # In words: only if you are not moving towards left of the screen (west), then turn the direction to right (east), as we
    # are not allowed to turn left or right when in a horizontal line.

    def add_tail(self):
        tail = tu.Turtle() #this line and below are repetitive. Same as in create biggie.
        # we can make it better by creating a new function
        tail.shape("square")
        tail.color("white")
        tail.penup()
        x_cord1= self.biggie_list[-1].xcor()
        y_cord1=self.biggie_list[-1].ycor()
        tail.goto(x_cord1,y_cord1)
        self.biggie_list.append(tail)

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

    def move_left(self): #when a straight line horizontally, left and right should not work
        direction= self.biggie_list[0].heading()
        # if direction == 0:
        #     self.biggie_list[0].left(-180)
        if direction==90:
            self.biggie_list[0].left(90)
        elif direction==270:
            self.biggie_list[0].right(90)

    def move_right(self): #when a straight line horizontally, left and right should not work
        direction= self.biggie_list[0].heading()
        if direction==90:
            self.biggie_list[0].right(90)
        elif direction==270:
            self.biggie_list[0].left(90)