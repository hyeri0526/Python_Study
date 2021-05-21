import turtle as t
t.shape('turtle')

for i in range(4):
    t.pendown()
    colorList=["yellow", "red", "blue", "green"]
    t.fillcolor(colorList[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()
    t.forward(50)
    
t.exitonclick()