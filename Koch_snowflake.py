import turtle

turtle.screensize(1000, 400, "black")
turtle.setup(1000)
turtle.penup()
turtle.pensize(2)
turtle.goto(-500, 200)

turtle.pendown()
turtle.hideturtle()

n = 1 # order


def color(n):
    if n % 3 == 1:
        turtle.pencolor('magenta')
    elif n % 3 == 2:
        turtle.pencolor('blue')
    else:
        turtle.pencolor('green')


def koch_curve(n, len=700):
    if n == 0:
        turtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            koch_curve(n - 1, len / 3)


for i in range(3):
    color(n)
    koch_curve(n)
    turtle.right(120)  # 3*120=360

turtle.done()
