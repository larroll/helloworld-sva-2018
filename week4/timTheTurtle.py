import turtle
wn=turtle.Screen()
wn.bgcolor(0.2, 1.0, 0.6)
wn.title("Tim the Turtle says hello!")
wn.screensize(500,500)

tim = turtle.Turtle()
tim.pensize(5)
tim.pencolor("blue")


dot_distance = 25
width = 3
height = 3

tim.penup()

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(0,200)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(0,-200)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(-200,-200)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(200,0)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(-200,0)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(200,200)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(-200,200)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)

tim.goto(200,-200)

for y in range(height):
    for i in range(width):
        tim.dot()
        tim.forward(dot_distance)
    tim.backward(dot_distance * width)
    tim.right(90)
    tim.forward(dot_distance)
    tim.left(90)


turtle.done()