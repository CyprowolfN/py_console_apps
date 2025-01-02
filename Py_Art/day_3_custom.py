import turtle
 
# function draw a new petal
def petal(t, radius, angle):
    for i in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
 
# function draw a new flower
def flower(t, numpetals, radius, angle):
    for i in range(numpetals):
        petal(t, radius, angle)
        t.left(360 / numpetals)
 
# function to move to a different position to draw a new flower   
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
 
# start of main program
window = turtle.Screen()
window.bgcolor("#3e4b4f")
 
t = turtle.Turtle()
# t.shape("turtle")

# draw flower 1 SHADED_GREEN
t.color("#1c6124")
move(t, 0)
t.begin_fill()
flower(t, 14, 200.0, 60.0)
t.end_fill()

# draw flower 2 LIT_GREEN
t.color("#5ba345")
move(t, 0)
t.begin_fill()
flower(t, 7, 150.0, 70.0)
t.end_fill()

# draw flower 3 SHADED_GREEN
t.color("#1c6124")
move(t, -350)
t.begin_fill()
flower(t, 14, 80.0, 60.0)
t.end_fill()

# draw flower 4 LIT_GREEN
t.color("#5ba345")
move(t, 0)
t.begin_fill()
flower(t, 7, 60.0, 70.0)
t.end_fill()

# draw flower 5 SHADED_GREEN
t.color("#1c6124")
move(t, 700)
t.begin_fill()
flower(t, 14, 80.0, 60.0)
t.end_fill()

# draw flower 6 LIT_GREEN
t.color("#5ba345")
move(t, 0)
t.begin_fill()
flower(t, 7, 60.0, 70.0)
t.end_fill()


turtle.mainloop()

ask = (input("All done?"))