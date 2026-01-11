import calendar
import turtle
def get_date_info():
    while True: 
        try:
            year = int(input("Enter the year: "))
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day: "))
            day_index = calendar.weekday(year, month, day)
            list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            result_day = list_of_days[day_index]
            print(calendar.month(year, month))
            print(day, month, year, result_day)
        except ValueError:
            print("ERROR: Please enter numbers only!")
            return
        except IndexError:
            print("ERROR: Invalid date!")
            return
        final_txt = f"{day:02d}/{month:02d}/{year} {result_day}"
        return year, month, day, final_txt

def get_user_notes():
    user_notes = {}
    while True:
        try:
            day_input = int(input("Enter the day which you want to add a note (If you don't want to add any note, write '0'): "))
        except ValueError:
            print("ERROR: Please enter numbers only!")
            continue
        if day_input != 0:
            notes_input = input(f"Enter your note for {day_input}. day: ")
            if day_input in user_notes:
                user_notes[day_input].append(notes_input)
            else:
                user_notes[day_input] = [notes_input]
            print("Note added for day ", day_input)
        else:
            print("Finished adding notes!")
            break
    return user_notes

def draw_calendar(year, month, txt, notes_data):
    wn = turtle.Screen()
    wn.bgcolor("darkblue")
    wn.title("Interactive Calendar")

    pen = turtle.Turtle()
    pen.color("white")
    pen.speed(0)
    pen.hideturtle()

    pen.penup()
    pen.goto(-175, 150)
    pen.pensize(4)
    pen.pendown()
    for i in range(2):
        pen.forward(350)
        pen.right(90)
        pen.forward(220)
        pen.right(90)
    pen.penup()

    pen.goto(0, -50)
    pen.write(calendar.month(year, month), align = "center", font = ("Courier", 20, "italic"))

    pen.goto(0, 185)
    pen.color("lightpink")
    pen.write(txt, align = "center", font = ("Arial", 22, "bold"))
    
    pen.goto(50, -200)
    pen.color("yellow")
    pen.write("YOUR NOTES: ", align = "left", font = ("Arial", 16, "italic"))
    
    if notes_data != {}:
        y_cor = -230
        for key, value in notes_data.items():
            pen.goto(50, y_cor)
            notes = f"{key} {calendar.month_name[month]}: {','. join(value)}"
            pen.write(notes, align = "left", font = ("Arial", 14, "italic"))
            y_cor -= 20
    else:
        pen.goto(50, -230)
        pen.write("No notes added.", align = "left", font = ("Arial", 14, "italic"))

    wn.exitonclick()

year, month, day, final_txt = get_date_info()
user_notes_data = get_user_notes()
draw_calendar(year, month, final_txt, user_notes_data)