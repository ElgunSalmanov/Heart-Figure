import turtle
import math


def xt(t):
    return 16 * math.sin(t) ** 3


def yt(t):
    return (
        13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    )


t = turtle.Turtle()
t.speed(10000000000000)
turtle.colormode(255)
turtle.Screen().bgcolor(220, 200, 220)

for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((250 - i) % 240, i % 230, (220 + 1) // 2 % 210)
    t.goto(0, 0)

t.hideturtle()
turtle.update()
turtle.mainloop()
