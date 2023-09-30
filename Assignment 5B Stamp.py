#Taylor Shook
#COP 2500
#Date:2/28/2023
#Assignment: 5B Travel Stamps

import turtle
import random
import math

#####
# This stamp is mine
def taylor_shook_stamp(posx,posy):

    #positioning turtle
    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(posx,posy)
    turtle.speed(10)

    #settting turtle to fill, size and color I want
    turtle.color("#04c984")
    turtle.fillcolor("#8cf5d0")
    turtle.pensize(6)

 
    #Draw 3 circles that are connected
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

    #Drawing three large rings around the three circles
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


#####
#This Stamp is from David Grissom  MW12pm
def david_grissom_stamp(x,y):
    import turtle
    import random
    t = turtle.Turtle()
    turtle.colormode(255)
    t.speed(4)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    
    def star():
        """draws a simple 5 point star filled gold"""
        t.setheading(0)
        t.color("gold")
        t.begin_fill()
        for i in range(5):
            t.forward(25)
            t.right(144)
        t.end_fill()

    #draws a 150 x 150 border and goes to center
    t.pencolor(255,0,0)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.penup()
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.setheading(0)
    t.pendown()

    #loop that randomizes the color for each line of the spiral square
    for i in range(56):
        r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        t.pencolor(r,g,b)
        t.forward(i*2)
        t.right(91)

    #top right star
    t.penup()
    t.setheading(0)
    t.forward(25)
    t.setheading(-90)
    t.forward(20)
    t.pendown()
    star()

    #bottom right star
    t.penup()
    t.setheading(-90)
    t.forward(100)
    t.pendown()
    star()

    #bottom left star
    t.penup()
    t.setheading(180)
    t.forward(105)
    t.pendown()
    star()

    #top left star
    t.penup()
    t.setheading(90)
    t.forward(100)
    t.pendown()
    star()


#####
#This Stamp is from Ricardo Nieto MW12
def ricardo_nieto_stamp(posX, posY):
    turtle.penup()
    turtle.goto(posX,posY)
    turtle.pendown()

    #Triangular Base of stamp(Triangles simbolize the Creative Spirit, whi is something that describe me because I like to develop and cerate new things)

    turtle.fillcolor("#C9F8F9")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()
    
    #2 Circular Bases of stamp(two circles together represents union and comintmet, which decribes my character) 
    turtle.fillcolor("#F8E2DD")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor("#272E2E")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    #Name initial R with cone in middle(represents my name)
    turtle.fillcolor("#EFFF02")
    turtle.begin_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.left(40)
    turtle.forward(5)
    turtle.left(50)
    turtle.forward(47)
    turtle.left(90)
    turtle.forward(26)
    turtle.penup()
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor("#272E2E")
    turtle.begin_fill()
    for i in range (4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

    #Dobble triangle simbol right( means balance and the search for stability, which is something I am looking for in my life)
    turtle.penup()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.fillcolor("#E0E716")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(30)
        turtle.right(120)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    for i in range(3):
        turtle.forward(30)
        turtle.right(120)
    turtle.end_fill()

   #Doble Triangle simbol left (means balance and the search for stability, which is something I am looking for in my life)
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.pendown()
    
    turtle.fillcolor("#E0E716")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(30)
        turtle.right(120)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    for i in range(3):
        turtle.forward(30)
        turtle.right(120)
    turtle.end_fill()



def main():
    taylor_shook_stamp(-300,-300)
    taylor_shook_stamp(300,300)
    ricardo_nieto_stamp(100,150)
    ricardo_nieto_stamp(1,20)
    david_grissom_stamp(-300,300)
    david_grissom_stamp(300,-300)
    

main()
    




