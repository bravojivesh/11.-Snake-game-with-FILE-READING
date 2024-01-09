import random
import turtle as tu
import time

screen1=tu.Screen()
screen1.bgcolor("black")
screen1.tracer(0) #tracer(0): This turns off animation completely.
# It means the screen won't update until the entire drawing is complete, which might make the process seem faster but won't show the drawing process.
#We have to call screen.update() when used with 0 else it wont display anythign.

# biggie.shapesize(stretch_len=9) #the instructor wants us to create using "multiple instances" of snake as opposed
#to using one square with a longer length

x_cord=0
y_cord=0

positions=[(x_cord,y_cord), (x_cord-20,y_cord),(x_cord-40,y_cord)]
biggie_list=[]
keep_moving= True

# for i in range (10):
#     biggie.goto(x_cord,y_cord)
#     biggie.forward(20)
#     x_cord+=20
#JH:The above was my initial code but it will not work. Why? Because it will move the same object (Biggie) back and forth.
# We want new instances (multiple Biggies) and not just one instance being worked on.


for i in range(3):
    biggie = tu.Turtle()
    biggie.shape("square")
    biggie.color("white")
    biggie.penup()
    biggie.goto(positions[i])
    biggie_list.append(biggie) #we need to keep track of all the Biggies

print (biggie_list) #just for my understanding that it is a "list of objects"
print (len(biggie_list))

while keep_moving:
    screen1.update()
    time.sleep(0.15)
    for b in range(len(biggie_list)-1,0,-1): #we want to start from the end and move each piece one step ahead.
        # So this means: it will return only an INTEGER. And the stop value is NOT INCLUSIVE. So if length is 3, then only 2 and 1.
        #the first piece is NOT in the loop. We have to mention outside of the loop to move it one step ahead.
       print (b)
       new_x = biggie_list[b-1].xcor() #grabbing the x-cordinate of the piece that is one step before. When b is the last one, this will be for one step ahead of b.
       new_y = biggie_list[b-1].ycor() #grabbing the y-cordinate of the piece that is one step before.
       biggie_list[b].goto(new_x,new_y) #telling that last piece to go to "the position that is one step ahead"
    biggie_list[0].forward(20)

screen1.exitonclick()