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
window.bgcolor("Yellow")
 
t = turtle.Turtle()
t.shape("turtle")
 
# draw flower 1
t.color("green")
move(t, -150)
t.begin_fill()
flower(t, 7, 60.0, 60.0)
t.end_fill()
 
# draw flower 2
t.color("red")
move(t, 150)
t.begin_fill()
flower(t, 10, 30.0, 70.0)
t.end_fill()
 
# draw flower 3
t.color("blue")
move(t, 150)
t.begin_fill()
flower(t, 14, 70.0, 50.0)
t.end_fill()
 
turtle.mainloop()

ask = (input("All done?"))