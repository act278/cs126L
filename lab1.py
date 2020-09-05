import turtle
import math

#givens
tmin = 0 
gravity = 9.807
deltat = 0.05

#prompted
angle = float(input("Enter an angle: "))
velocity_init = float(input("Enter the initial velocity: "))
tmax = float(input("Enter the time duration: "))
height_init = float(input("Enter the initial height: "))

apple = turtle.Turtle()

def main():
    n = 0
    apple.pendown()
    apple.backward(500)
    apple.forward(1000)
    apple.penup()
    apple.goto(0,height_init)
    while(n < tmax):
        y = height_init + velocity_init*math.sin(angle)*n - 0.5*gravity*(n**2)
        x = velocity_init*math.cos(angle)*n
        apple.pendown()
        apple.goto(x,y)
        n += deltat
        if((n > velocity_init*math.sin(angle) / gravity) & (y <= 0)):
            break

main()
turtle.Screen().exitonclick()