import turtle #imports turtle

def GreenArrow(): #goes to location and draws the boarder
    turtle.penup()
    turtle.speed(0)
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.color('green')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.goto(0,-175)
    turtle.color('white')
    turtle.begin_fill()
    turtle.circle(175)
    turtle.end_fill()

def GreenArrow1(): #imports GreenArrow() and then draws the arrow
    GreenArrow()
    turtle.begin_fill()
    turtle.color('dark green')
    turtle.goto(0,200)
    turtle.right(70)
    turtle.forward(320)
    turtle.right(60)
    turtle.forward(100)
    turtle.right(50)
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.right(50)
    turtle.forward(320)
    turtle.end_fill()

def Flash():       #goes to location and draws the boarder
    turtle.penup()
    turtle.speed(0)
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.goto(0,-175)
    turtle.color('white')
    turtle.begin_fill()
    turtle.circle(175)
    turtle.end_fill()

def Flash1():     #imports Flash() and draws the lightning bolt
    Flash()
    turtle.color('orange')
    turtle.penup()
    turtle.goto(170,200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(130)
    turtle.forward(175)
    turtle.right(-120)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(150)
    turtle.right(-120)
    turtle.forward(60)
    turtle.right(120)
    turtle.forward(230)
    turtle.right(160)
    turtle.forward(130)
    turtle.right(-95)
    turtle.forward(50)
    turtle.right(110)
    turtle.forward(130)
    turtle.right(-110)
    turtle.forward(50)
    turtle.right(125)
    turtle.forward(300)
    turtle.end_fill()
    