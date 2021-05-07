def func1(a):  # a는 지역변수
    a = a + 5
    print(a)
    return a
def func2(i):  # i, b는 지역변수
    print(b)
    print(i)
   # print(k) 는 정의되지 않아 에러
    
a = int(input("정수입력"))  # a, b는 전역변수
print(a)
b = func1(a)
print(a)
print(b)
func2(6)
