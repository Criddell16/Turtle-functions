import turtle #imports turtle

x = -200  #starting location
y = 200

def board1(x,y):             #creates the boards squares
    turtle.pensize(0.001)
    turtle.goto(x,y)
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def outline():                #creates the outline for the board
    turtle.color('white')
    turtle.goto(-200,200)
    turtle.pensize(5)
    turtle.color('blue')
    turtle.penup()
    for i in range(4):
        turtle.pendown()
        turtle.forward(400)
        turtle.right(90)
    turtle.penup()
