import random
import math
import turtle

distance = 1
needles = int(input("Enter the amount of needles: "))
distanceLine = 0


def main():
    print(buffonNeedle())


def showMontePi(numDarts):
    wn = turtle.Screen()
    drawingT = turtle.Turtle()

    wn.setworldcoordinates(-2, -2, 2, 2)

    drawingT.up()
    drawingT.goto(-1, 0)
    drawingT.down()
    drawingT.goto(1, 0)

    drawingT.up()
    drawingT.goto(0, 1)
    drawingT.down()
    drawingT.goto(0, -1)

    inCircle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        drawingT.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pi = inCircle / numDarts * 4
    wn.exitonclick()

    return pi


def buffonNeedle():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(10)
    screen.setworldcoordinates(0, 0, 3, 3)
    buffStartUp(t)
    intersect = 0
    for _ in range(needles):
        # Set default color (non-intersecting)
        color = "#6ca641"
        angle = random.randint(0, 180)
        x = random.uniform(0.5, 2.5)
        y = random.uniform(0.5, 2.5)
        # Determines distance to nearest line
        if((y <= 1.5) & (y > 1)):
            distanceLine = y - 1
        elif(y <= 1):
            distanceLine = 1 - y
        elif((y > 1.5) & (y < 2)):
            distanceLine = 2 - y
        elif(y >= 2):
            distanceLine = y - 2
        # Determines if the needle intersects a line
        if(distanceLine <= math.sin(math.radians(angle))*.5):
            intersect += 1
            color = "#3259c2"
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()
        t.color(color)
        t.forward(distance/2)
        t.backward(distance)
        t.penup()
        if(intersect == 0):
            return ("Operation cancelled due to no intersecting lines. "
                    "Please try again by entering more needles.")
    return 2*(needles/intersect)


def buffStartUp(t):
    # Draws the 2 lines
    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(3, 1)
    t.penup()
    t.goto(0, 2)
    t.pendown()
    t.goto(3, 2)
    t.penup()


main()
turtle.Screen().exitonclick()
