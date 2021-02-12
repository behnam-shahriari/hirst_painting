import turtle as t
import random

color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

hirst = t.Turtle()
screen = t.Screen()

hirst.shape('arrow')
hirst.hideturtle()
screen.colormode(255)
hirst.speed("fastest")
hirst.penup()
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)


x = hirst.xcor()
y = hirst.ycor()
count = 0


while count != 10:
    for _ in range(10):
        hirst.pencolor(random.choice(color_list))
        hirst.dot(20)
        hirst.penup()
        hirst.fd(50)
    y = y + 50
    hirst.goto(x, y)
    count += 1

screen.exitonclick()
