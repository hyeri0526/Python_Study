import turtle as t
import random as r

for i in range(30):
    length = r.randint(1, 100)
    t.forward(length)
    angle = r.randint(-180, 180)
    t.left(angle)
    
t.done()
t.bye()