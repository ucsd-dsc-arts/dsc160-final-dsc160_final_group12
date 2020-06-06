from random import choice
def draw_word(colors):
    
    number= random.choice([0,1,2])
    if number==1:
        #draw hexogram-sprial
        setup()
        title("hexogram sprial")
        t1 = Turtle()
        bgcolor('black')

        #hide the turtle icon
        t1.hideturtle()
        t1.speed(0)
        for i in range (200):
            #choose a random color for the turtle
            colorchoice = choice(colors)
            #have the turtle take on the randomly chose color
            t1.color(colorchoice)
            t1.forward(i)
            t1.left(59)
        #t1.done()
        try:
            t1.exitonclick()   
        except Excpetion:
            pass
    elif number==2:
        #draw color spirograph
        setup()
        title("spirograph")
        #create a turtle for drawing
        t1 = Turtle()
        bgcolor('black')
        #change the pen thickness
        t1.width(2)
        #hide the turtle icon
        t1.hideturtle()
        #set turtle speed to MAXIMUM (1-10 for specific speeds. 1 is slowest)
        t1.speed(0)

        #create a loop for the graphics to be built
        for i in range(50):
            #choose a random color for the turtle
            colorchoice = choice(colors)
            #have the turtle take on the randomly chose color
            t1.color(colorchoice)
            #create circle
            t1.circle(100)
            t1.left(10)

        #t1.done()
        try:
            t1.exitonclick()   
        except Excpetion:
            pass
    else:
        #color wheel
        setup()
        title("colorwheel")
        t1 = Turtle()
                    #do some basic setup for the turtle
        #pick up the pen so no marks are left
        t1.up()
        #move the turtle to the left
        t1.goto(-200,0)
        #put the pen back down
        t1.down()
        #change the pen thickness
        t1.width(2)
        #hide the turtle icon
        t1.hideturtle()
        #set turtle speed to MAXIMUM (1-10 for specific speeds. 1 is slowest)
        t1.speed(0)

        #create a loop for the graphics to be built
        for i in range(500):
            #choose a random color for the turtle
            colorchoice = choice(colors)
            #have the turtle take on the randomly chose color
            t1.color(colorchoice)
            #move the turtle forward
            t1.forward(400)
            #have the turtle turn 181 degrees (anything over 180 works)
            t1.right(181)

        #t1.done() 
        try:
            t1.exitonclick()   
        except Excpetion:
            pass