import turtle as tu

screen1=tu.Screen()
screen1.bgcolor("black")
screen1.listen()

biggie=tu.Turtle()
biggie.shape("square")
biggie.shapesize(stretch_len=9)
biggie.color("white")

while screen1.onkey():
    biggie.forward(20)

print (biggie.position())










screen1.exitonclick()