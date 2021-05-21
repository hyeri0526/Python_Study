import turtle as t
t.shape("turtle")

while True:
    s=t.textinput("", "도형의 종류를 입력하세요.")
    t.reset()    
    if s=="사각형":
        sw=t.textinput("", "가로:")
        w=int(sw)
        sh=t.textinput("","세로:")
        h=int(sh)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)    
    elif s=="삼각형":
        sl=t.textinput("", "길이:")
        w=int(sl)
        t.forward(w)
        t.left(120)
        t.forward(w)
        t.left(120)
        t.forward(w)
    elif s=="원":
        sr=t.textinput("", "반지름:")
        r=int(sr)
        t.circle(r)
    else:
        t.write("사각형, 삼각형, 원 중에 하나를 입력하세요.")
        
t.exitonclick()