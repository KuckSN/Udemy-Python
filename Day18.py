# import colorgram

# colors = colorgram.extract("image.jpg", 10)
# rgd_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgd_colors.append((r, g, b))

# print(rgd_colors)

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_dots = 100

for count in range(1, number_dots+1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
# from turtle import Turtle, Screen
# import turtle
# import random

# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("red", "yellow")

# def dashed():
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# def move():
#     timmy.forward(100)
#     timmy.right(90)

# def shape(num_sides):
#     angle = 360 / num_sides

#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# # timmy.pensize(15)
# timmy.speed("fastest")
# turtle.colormode(255)

# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     return (r, g, b)

# def random_walk():    
#     timmy.color(random_colour())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# def circle(deviation):
#     for i in range(round(360/deviation)):
#         timmy.color(random_colour())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+deviation)


# circle(5)


# screen = Screen()
# screen.exitonclick()


