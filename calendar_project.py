import calendar
import turtle
def show_calendar():
    try:
        year_input = int(input("Enter the year: "))
        month_input = int(input("Enter the month (1-12): "))
        day_input = int(input("Enter the day: "))
        day_index = calendar.weekday(year_input, month_input, day_input)
        list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        result_day = list_of_days[day_index]
        print(calendar.month(year_input, month_input))
        print(day_input, month_input, year_input, result_day)
    except ValueError:
        print("ERROR: Please enter numbers only!")
        return
    except IndexError:
        print("ERROR: Invalid date!")
        return
    final_txt = f"{day_input:02d}/{month_input:02d}/{year_input} {result_day}"

    sam = turtle.Turtle()
    sam.color("white")
    sam.speed(6)
    sam.hideturtle()
    wn = turtle.Screen()
    wn.bgcolor("darkblue")
    wn.title("Day Finder")

    sam.penup()
    sam.goto(-175, 120)
    sam.pensize(4)
    sam.pendown()
    for i in range(2):
        sam.forward(350)
        sam.right(90)
        sam.forward(300)
        sam.right(90)
    sam.penup()

    sam.goto(0, -120)
    sam.write(calendar.month(year_input, month_input), align = "center", font = ("Courier", 20, "italic"))
    sam.goto(0, -220)
    sam.color("lightpink")
    sam.write(final_txt, align = "center", font = ("Arial", 24, "bold"))
    wn.exitonclick()

show_calendar()