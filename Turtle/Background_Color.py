import turtle

t = turtle.Turtle()

t.screen.bgcolor("orange")

x = t.screen.window_width() // 2
y = t.screen.window_height() // 2

print((-x, y), (x, -y))

turtle.exitonclick()