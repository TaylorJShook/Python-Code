#Taylor Shook
#COP 2500
#Date:2/15/2023
#Assignment: 5A Travel Stamps

import turtle, random

#positioning turtle
turtle.penup()
turtle.forward(20)
turtle.speed(10)

#settting turtle to fill, size and color I want
turtle.color("#04c984")
turtle.fillcolor("#8cf5d0")
turtle.pensize(6)

#The three circles interconnected represent my family and I
#They are the color green because green is my favorite color
#The middle size represents me, large is my boyfriend and the small is our dog
#Both the color green and my family makes me happy
turtle.pendown()
turtle.begin_fill()
for i in range(3):
    turtle.circle(40-(i*10))
    turtle.right(100)
turtle.end_fill()


#positioning turtle for larger circles
turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.right(180)
turtle.forward(50)
turtle.right(45)
turtle.forward(40)
turtle.left(90)
turtle.backward(10)

# The large ring of circles is colored variations of blue and meant to look like a bubble
#The bubble represents the safe space and environment.

for i in range(3):
    num=random.randint(1,10)
    if(num>5):
        turtle.color("#6176ff")
    else:
        turtle.color("#909efc")
        
    turtle.pensize(10-(i*3))
    turtle.pendown()
    turtle.circle(80+(i*10))
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)

    


