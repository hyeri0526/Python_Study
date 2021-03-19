a= 3
b= ~a #a의 1의 보수
print(a, b, "b=b+1=>", (b+1)) #b+1은 2의 보수

a = 3
b = 5
c = a & b # AND 2진수에서 둘 중에 하나라도 0이면 0(둘 다 1이면 1)
print(a, b, c)

a = 3
b = 5
c = a ^ b # exclusive OR 두 개가 같으면 0 다르면 1
print(a, b, c)

a = 3
b = 5
c = a | b # OR 두 개 중에 하나라도 1이면 1(둘 다 0이면 0)
print(a, b, c)
