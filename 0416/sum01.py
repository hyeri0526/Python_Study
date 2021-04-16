print("이혜리")
print("202106028")
print("이혜리", end=":")  #줄을 바꾸지 않고 다음 내용 출력
print("202106028")

num=int(input("정수 입력:"))
sum = 0
for i in range(1,(num+1)):
    if i <num:
        print(i,"+ ", end="")
    else:
        print(i,"= ", end="")
    sum += i
print(sum)
