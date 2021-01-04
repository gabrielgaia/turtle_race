from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-60, -30, 0, 30, 60, 90]
turtle_list = []
is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)
screen.title("Welcome to the Turtle Race!")

user_guess = screen.textinput("It's time to bet!", "Which turtle you will? Enter a color: ")

for turtle_index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle.speed("slow")
    turtle_list.append(turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_guess.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            is_race_on = False
            break

screen.exitonclick()
