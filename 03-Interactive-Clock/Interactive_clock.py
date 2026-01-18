import turtle
import datetime
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Interactive Clock")
wn.setup(width=600, height=600)

def draw_clock():
    pen = turtle.Turtle()
    pen.color("white")
    pen.shape("square")
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(5)
    pen.left(90)
    pen.stamp()

    for i in range (12):
        pen.penup()
        pen.goto(0,0)
        pen.right(30)
        pen.forward(175)
        pen.pendown()
        pen.forward(50)
        pen.penup()
        if 2 < i < 8:
            pen.forward(45)
        else:
            pen.forward(30)
        pen.write(f"{i+1}", align = "center", font=("Courier", 18, "bold"))
    
def draw_current_info():
    info_pen = turtle.Turtle()
    info_pen.hideturtle()
    info_pen.color("cyan")
    info_pen.penup()
    info_pen.goto(400, -350)

    now = datetime.datetime.now()
    time_txt = now.strftime("%H:%M:%S")
    date_txt = now.strftime("%d %B %Y %A")

    current_txt = f"{date_txt}\n{time_txt}"
    info_pen.write(current_txt, align="left", font=("Courier", 18, "italic"))

def draw_hands():
    now = datetime.datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12

    hour_angle = hour * 30
    min_angle = minute * 6
    sec_angle = second * 6

    hour_hand = turtle.Turtle()
    hour_hand.shape("arrow")
    hour_hand.color("#FFFFFF")
    hour_hand.shapesize(stretch_wid=0.8, stretch_len=9)
    hour_hand.left(90)
    hour_hand.right(hour_angle)

    minute_hand = turtle.Turtle()
    minute_hand.shape("arrow")
    minute_hand.color("#10CEDC")
    minute_hand.shapesize(stretch_wid=0.6, stretch_len=12)
    minute_hand.left(90)
    minute_hand.right(min_angle)

    second_hand = turtle.Turtle()
    second_hand.shape("arrow")
    second_hand.color("#BA0FF8")
    second_hand.shapesize(stretch_wid=0.4, stretch_len=15)
    second_hand.left(90)
    second_hand.right(sec_angle)


draw_clock()
draw_current_info()
draw_hands()

wn.exitonclick()

#Ideas: sağ üst köşede current date and time (input ile kullanıcıdan yerel saati al)
# kronometre (başlat/durdur/sıfırla/tur), sayaç(input: kaç dk olsun) sayaç sonrası bitti animasyonu, 
# 
#  