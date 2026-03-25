import turtle, math
wn = turtle.Screen()
wn.bgcolor("lightgreen")
# Attempting to draw a soccer field.
alain = turtle.Turtle()
alain.color("red")
alain.speed(5) #Increase the printing speed
alain.pensize(5)
alain.penup()
alain.goto(150, 50)
alain.pendown()
for i in range(2):
    alain.backward(300)
    alain.right(90)
    alain.forward(100)
    alain.right(90)
def lines_inside(solid, doted):
    alain.pensize(1)
    alain.backward(150)
    alain.right(90)
    alain.forward(solid)
    alain.dot(doted) #draw doted center of the field
    alain.forward(2) #distance between dots
    alain.right(90)
    alain.penup()
    alain.forward(150)
    alain.pendown()
    alain.right(90)
    alain.forward(25)
    alain.right(90)
    alain.forward(25)
    alain.right(90)
    alain.forward(50)
    alain.right(90)
    alain.forward(25)
    alain.penup()
    alain.backward(300)
    alain.pendown()
    alain.forward(25)
    alain.right(90)
    alain.forward(50)
    alain.right(90)
    alain.forward(25)
    alain.penup()
    alain.backward(150)
    alain.right(90)
    alain.pendown()
    alain.forward(70)
    alain.penup()
    alain.goto(-2, 60) # To center the field in the middle
    alain.write("Alan Soccer Field", align='center',font=("Arial",30,("bold","normal"))) #Name the field
lines_inside(50, 40) # just wanted to you the def function

print("Alain")
wn.exitonclick()