from turtle import *


#we want to paint house

#step1: draw a square
speed(30)
width(6)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing dor

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#Draw first window
penup()
goto(15, 180)  
pendown()

color("light blue")
begin_fill()
left(120)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
right(90)
forward(60)
end_fill()



#draw secend window
penup()
goto(185, 180)
pendown()

color("light blue")
begin_fill()
left(90)
forward(45)
left(90)
forward(60)
left(90)
forward(45)
left(90)
forward(60)
end_fill()








exitonclick()