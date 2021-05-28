import turtle as t

def drawRect(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
for i in range(-200,400,200): # (start,end,step)
    t.up()
    t.goto(i,0)
    t.down()
    drawRect(100)


t.done()
t.bye()