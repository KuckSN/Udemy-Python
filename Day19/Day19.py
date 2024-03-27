from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wil win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()

            if winning_color.lower() == user_bet.lower():
                print(f"You Win")
                is_race_on = False
            
            else:
                print("You lose")
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

