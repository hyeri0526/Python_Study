import turtle as t

s=t.textinput("input", "몇 각형을 원하세요.")
n=int(s)

for i in range(n):
    t.forward(500)
    t.left(360/n)
    
t.done()