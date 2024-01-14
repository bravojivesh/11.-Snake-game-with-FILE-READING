import biggie2
# OR biggie. Biggie2 has more concise code
import turtle as tu
import time
import food
from score import Score

eog=False

screen1=tu.Screen()
screen1.bgcolor("grey")
screen1.tracer(0)
screen1.listen()

k=biggie2.Biggie()
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

    for member in k.biggie_list:
        if member!=head and head.distance(member.position()) <5:
            score1.game_over()
            eog= True

    if head.xcor() >365 or head.xcor() <-365 or head.ycor() >315 or head.ycor() <-315:
        score1.game_over()
        eog=True


    if head.distance (food1.xcor(),food1.ycor())<20:
        print ("yaay")
        food1.create_food()
        score1.update()
        k.add_tail()


screen1.exitonclick()