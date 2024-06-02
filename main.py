import turtle
from random import randint
from time import sleep
import threading

# Ekranı ayarla
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("lightblue")
screen.title("Kaplumbağa Yakalama Oyunu")


# Kaplumbağa oluştur
efe = turtle.Turtle()
efe.shape("turtle")
efe.turtlesize(3)
efe.color("green")
efe.penup()

# Teleport
def teleport(x, y):
    efe.penup()
    efe.setpos(x, y)
    efe.pendown()

# Ekran üstüne yazı yaz
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.goto(0, 350)  #
yazi.write("Kaplumbağa Yakalama Oyunu", align="center", font=("Arial", 16, "bold"))


def sayac():
    sayac_turtle = turtle.Turtle()
    time_off = 20
    style = ('Courier', 30, 'italic')
    while time_off >= 0:
        sayac_turtle.hideturtle()
        sayac_turtle.penup()
        sayac_turtle.goto(0, 300)
        sayac_turtle.clear()
        sayac_turtle.write(time_off, font=style, align='center')
        sleep(1)
        time_off -= 1
    sayac_turtle.clear()
    sayac_turtle.write("Time's up!", font=style, align='center')

# Kaplumbağa rastgele hareket etsin.
while True:
    sleep(1)
    efe.hideturtle()
    rand = randint(-300, 300)
    rand2 = randint(-300, 300)
    teleport(rand, rand2)
    efe.showturtle()
    sayac()



turtle.mainloop()