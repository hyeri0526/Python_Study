def func3(a=1, b=1):  #인수 없을 때 a=1, b=1로 정함.
    c = a + b
    return c
a = 6
b = func3(a, 5)
print(b)
b = func3(a, 1)
print(b)
b=func3(a)   # 인수를 하나만 주면 첫번째에 들어감.
print(b)
b=func3()
print(b)
