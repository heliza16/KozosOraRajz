import turtle

#Liza első óra mutató vonal megrajzolása
turtle.color("green")
turtle.left(130)
turtle.forward(200)
turtle.right(90)


#Mária második óra mutató vonal megrajzolása
turtle.penup()
turtle.setposition(0,0)
turtle.pendown()
turtle.pensize(5)
turtle.color("magenta")
turtle.setheading(90)
turtle.forward(200)

#harmadik mutattó
turtle.left(180)
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.color("skyblue")
turtle.pensize(15)
turtle.left(130)
turtle.forward(200)
turtle.left(180)
turtle.forward(200)
turtle.left(30)
turtle.color("black")
turtle.right(160)


turtle.done()