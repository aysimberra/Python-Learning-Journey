import turtle
import random
import time
wn = turtle.Screen()
wn.bgcolor("#9370DB")
wn.setup(width = 1000, height = 1000)
wn.title("Turtle Race")

def draw_lines():
    line = turtle.Turtle()
    line.color("black")
    line.pensize(4)
    line.speed(0)
    line.shape("square")
    line.penup()
    line.goto(-300, 165)
    line.pendown()
    line.stamp()
    line.goto(-300,-165)
    line.stamp()
    line.penup()

    line.goto(300, -165)
    line.pendown()
    line.stamp()
    line.goto(300, 165)
    line.stamp()
    line.hideturtle()

def start_race(user_guess, name1, name2):
    tom = turtle.Turtle()
    tom.color("#0C4646")
    tom.shape("turtle")
    tom.penup()
    tom.shapesize(2)
    tom.goto(-335,50)
    tom.write(name1, align = "right", font = ("Arial", 18, "bold"))
    tom.goto(-300, 50)
    tom.speed(3)

    bloom = turtle.Turtle()
    bloom.color("#A45A26")
    bloom.shape("turtle")
    bloom.penup()
    bloom.shapesize(2)
    bloom.goto(-335, -50)
    bloom.write(name2, align = "right", font = ("Arial", 18, "bold"))
    bloom.goto(-300, -50)
    bloom.speed(3)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 200)
    size = 26
    for i in range(3, 0, -1):
        pen.write(i, align = "center", font=("Arial", size, "bold"))
        time.sleep(1)
        pen.clear()
        size += 3
    pen.write("GO!!!", align = "center", font = ("Arial", 26, "bold"))
    time.sleep(1)
    pen.clear()

    race_continues = True
    while race_continues:
        tom.forward(random.randint(20,65))
        bloom.forward(random.randint(20,65))
        if tom.xcor()> 300 or bloom.xcor()> 300:
            race_continues = False
            if tom.xcor() > bloom.xcor():
                winner = name1
                tom.shapesize(3)
                print(f"{name1} won the race!")
            elif bloom.xcor() > tom.xcor():
                winner = name2
                bloom.shapesize(3)
                print(f"{name2} won the race!")
            else:
                winner = "tie"
                print("The race is a tie")
    
    if user_guess.lower() == winner.lower():
        message = f"Congratulations! Your guess was correct, {winner} won!"
    else:
        message = f"Unfortunately... You guessed {user_guess}, but {winner} won!"
    
    pen.write(message, align = "center", font = ("Arial", 20, "bold"))

first_racer = turtle.textinput("Name of racer", "Give a name to the 1st racer: ")
second_racer = turtle.textinput("Name of racer", "Give a name to the 2nd racer: ")
prediction = turtle.textinput("Make your bet", f"Which one do you think will win ({first_racer}/{second_racer}/Tie)?")

if prediction and first_racer and second_racer:
    draw_lines()
    start_race(prediction, first_racer, second_racer)
else:
    print("Game cancelled by user.")

wn.exitonclick()