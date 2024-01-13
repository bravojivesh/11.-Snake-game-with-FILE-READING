import biggie
import turtle as tu
import time
import food
from score import Score

eog=False

screen1=tu.Screen()
screen1.bgcolor("grey")
screen1.tracer(0)
screen1.listen()

k=biggie.Biggie()
# k.create_biggie() #remember it was running 6 times? If we put the create_biggie under class __init,
# we do not need to have this line.

head = k.biggie_list[0]
food1=food.Food()
food1.create_food()

score1=Score()

while eog==False:
    screen1.update()
    time.sleep(0.1)
    k.move_big_mackie()

    screen1.onkey(k.move_up,"Up")
    screen1.onkey(k.move_down, "Down")
    screen1.onkey(k.move_left, "Left")
    screen1.onkey(k.move_right, "Right")


    if head.distance (food1.xcor(),food1.ycor())<20:
        print ("yaay")
        food1.create_food()
        score1.update()


screen1.exitonclick()