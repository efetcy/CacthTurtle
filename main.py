import turtle
from random import randint

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
yazi.goto(0, 350)
yazi.write("Kaplumbağa Yakalama Oyunu", align="center", font=("Arial", 16, "bold"))

# Skoru tutacak değişken
skor = 0

# Skor yazıcısı
skor_yazi = turtle.Turtle()
skor_yazi.hideturtle()
skor_yazi.penup()
skor_yazi.goto(0, 320)
skor_yazi.write(f"Skor: {skor}", align="center", font=("Arial", 14, "bold"))

sayaç_durdu = False

# Sayaç fonksiyonu
def sayac(time_off):
    global sayaç_durdu
    sayac_turtle = turtle.Turtle()
    sayac_turtle.hideturtle()
    sayac_turtle.penup()
    style = ('Courier', 30, 'italic')

    def update_sayac():
        nonlocal time_off
        if time_off >= 0:
            sayac_turtle.clear()
            sayac_turtle.goto(0, 280)
            sayac_turtle.write(time_off, font=style, align='center')
            time_off -= 1
            screen.ontimer(update_sayac, 1000)
        else:
            sayac_turtle.clear()
            efe.hideturtle()
            sayac_turtle.write("Time's up!", font=style, align='center')

    update_sayac()

# Kaplumbağanın rastgele hareket etmesi
def kaplumbaga_hareket():
    if not sayaç_durdu:
        rand = randint(-300, 300)
        rand2 = randint(-300, 300)
        efe.hideturtle()
        teleport(rand, rand2)
        efe.showturtle()
        screen.ontimer(kaplumbaga_hareket, 1000)

# Kaplumbağaya tıklama olayı
def efe_tiklama(x, y):
    global skor
    if not sayaç_durdu:
        skor += 1
        skor_yazi.clear()
        skor_yazi.write(f"Skor: {skor}", align="center", font=("Arial", 14, "bold"))
        efe.hideturtle()


efe.onclick(efe_tiklama)

# Sayaç başlat
sayac(20)
kaplumbaga_hareket()

turtle.mainloop()