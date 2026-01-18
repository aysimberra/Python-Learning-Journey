import turtle
import datetime
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Interactive Clock")
wn.setup(width=800, height=800)
wn.tracer(0)

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

info_pen = turtle.Turtle()
info_pen.hideturtle()
info_pen.color("cyan")
info_pen.penup()
info_pen.goto(240, 300)

hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.color("#FFFFFF")
hour_hand.shapesize(stretch_wid=0.8, stretch_len=9)

minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.color("#10CEDC")
minute_hand.shapesize(stretch_wid=0.6, stretch_len=12)

second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.color("#BA0FF8")
second_hand.shapesize(stretch_wid=0.4, stretch_len=15)

def update_current_info():
    now = datetime.datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12

    time_txt = now.strftime("%H:%M:%S")
    date_txt = now.strftime("%d %B %Y %A")
    info_pen.clear()
    current_txt = f"{date_txt}\n{time_txt}"
    info_pen.write(current_txt, align="center", font=("Courier", 18, "italic"))

    hour_angle = 90 - (hour * 30) - (minute * 0.5)
    min_angle = 90 - (minute * 6)
    sec_angle = 90 - (second * 6)

    hour_hand.setheading(hour_angle)

    minute_hand.setheading(min_angle)

    second_hand.setheading(sec_angle)
    wn.update()

draw_clock()

try:
    while True:
        update_current_info()
        time.sleep(1)
except turtle.Terminator:
    pass