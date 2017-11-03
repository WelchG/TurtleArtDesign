def circle(t,x,y,size,dist):#Receiving values from RG file(RedGreen).
        t.penup()
        t.goto(x,y)
        t.pendown()
               
        for times in range(20): #Drawing the circle in RG file.
            t.begin_fill()
            t.color("red")
            t.circle(size)
            t.end_fill()
            t.penup()
            t.forward(dist)
            t.pendown()
            t.begin_fill()
            t.color("green")
            t.circle(size)
            t.end_fill()
            t.penup()
            t.forward(dist)
            t.pendown()

def snowflake(t,x,y,r,g,b):
        t.speed(0)
        t.color(r,g,b)
        t.width(5)
        t.circle(25,360)#Drawing the circle in the middle of the snowflake.

        a=45 #How much of a circle the turtle is drawing.

        for times in range(8):   
            t.circle(25,a)#Drawing the branches of the snowflake
            t.right(90)
            t.forward(100)
            t.backward(40)
            t.right(45)
            t.forward(40)
            t.backward(40)
            t.left(90)
            t.forward(40)
            t.back(40)
            t.right(45)
            t.back(60)
            t.left(90)


        t.penup()
        t.left(90)
        t.forward(25)
        t.pendown()

        for times in range(12):#Drawing the star in the middle of the snowflake.
                t.forward(50)
                t.right(70)
                t.forward(50)
                t.right(110)
                t.forward(50)
                t.right(70)
                t.forward(50)
                t.right(80)

        t.penup()
        t.goto(x,y)
        t.pendown()

