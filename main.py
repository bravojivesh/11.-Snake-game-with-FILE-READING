import biggie
import turtle as tu
import time

screen1=tu.Screen()
screen1.bgcolor("black")
screen1.tracer(0)

k=biggie.Biggie()
k.create_biggie()




screen1.update()
time.sleep(0.1)

# flag= True
#
# while flag==True:
#     screen1.update()
#     time.sleep(0.1)
#     j.move_big_mackie()


screen1.exitonclick()