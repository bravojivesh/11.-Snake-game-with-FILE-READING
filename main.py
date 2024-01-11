import biggie
import turtle as tu
import time

eog=False

screen1=tu.Screen()
screen1.bgcolor("black")
screen1.tracer(0)

k=biggie.Biggie()
k.create_biggie()

while eog==False:
    screen1.update()
    time.sleep(0.1)
    k.move_big_mackie()


screen1.exitonclick()