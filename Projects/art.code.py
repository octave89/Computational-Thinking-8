import turtle 
t = turtle.Turtle()
t.speed(150)
turtle.bgcolor("Black")


#First Shape 
t.penup()
t.goto(150, -150)
t.pendown()
colors = ("PeachPuff", "Yellow", "Gold")
for i in range(360):
    t.color(colors[i % 3])
    t.circle(i,50)

#Second Shape
t.penup()
t.goto(-150,-150)
t.pendown()
colors = ("SteelBlue", "MediumBlue", "LightBlue")
for i in range(260):
    t.color(colors[i % 3])
    t.circle(i,40)

#Second Shape
t.penup()
t.goto(-150,150)
t.pendown()
colors = ("LemonChiffon", "Violet", "AliceBlue")
for i in range(260):
    t.color(colors[i % 3])
    t.circle(i,40)

#Second Shape
t.penup()
t.goto(150,150)
t.pendown()
colors = ("MistyRose", "Silver", "Plum")
for i in range(140):
    t.color(colors[i % 3])
    t.circle(i,40)

turtle.exitonclick() 