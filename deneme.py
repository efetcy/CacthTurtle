import turtle
from time import sleep

sayac = turtle.Turtle()

time_off = 20

style = ('Courier', 30, 'italic')

while time_off >= 0:
    sayac.hideturtle()
    sayac.clear()
    sayac.write(time_off, font=style, align='center')
    sleep(1)
    time_off -= 1

turtle.clear()
turtle.write("Time's up!", font=style, align='center')

turtle.done()