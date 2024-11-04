import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#000000")
t.speed(10)

for _ in range(36):
    t.pencolor("red")
    t.circle(100)
    t.left(10)

turtle.done()
