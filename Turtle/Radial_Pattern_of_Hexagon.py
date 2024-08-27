# Draw a radial pattern with 10 hexagons

import turtle

t=turtle.Turtle()

def hexagon(t, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons (t, n, length):
    """Draws a radial pattern of n hexagons with the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(360/n)

radialHexagons (t,10,50)

turtle.exitonclick()