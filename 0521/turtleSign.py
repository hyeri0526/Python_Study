import turtle as t
t.clear()
t.penup()
t.goto(100,100)
t.write("여기로 오면 양수입니다.")
t.goto(100,0)
t.write("여기로 오면 0입니다.")
t.goto(100,-100)
t.write("여기로 오면 음수입니다.")

t.goto(0,0)
t.pendown()
s=t.textinput("부호", "정수를 입력하세요.")
n=int(s)

if n>0:
    t.goto(100,100)
elif n==0:
    t.goto(100,0)
else:
    t.goto(100,-100)
