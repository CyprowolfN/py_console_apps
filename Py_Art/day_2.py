from turtle import speed, bgcolor, colormode, fd, rt, pencolor
speed(15)
bgcolor('black')
r, g, b = 255, 0, 0

for i in range(255 * 2):
    colormode(255)

    if i < 255 // 3:
        g += 3
    elif i < (255 * 2) // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < (255 * 4) // 3:
        g -= 3
    elif i < (255 * 5) // 3:
        r += 3
    else:
        b -= 3
    
    fd(28 + i)
    rt(45)
    pencolor(r, g, b)
ask = (input("All done?"))