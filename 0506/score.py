marks = []
for i in range(5):
    scr = int(input("%d 번 학생의 성적: " %(i+1)))
    marks.append(scr) #입력 받은 점수를 리스트에 추가
print(marks)

number = 0
sum = 0
avg = 0

for i in marks:
    sum += i
    number = number +1
    if i >=60:
        print("%d번 학생은 %d점 이고 합격입니다." %(number,i))
    else:
        print("%d번 학생은 %d점 이고 불합격입니다." %(number,i))
avg=(sum/number)
print("총 합은 %d이고 평균은 %f입니다."%(sum, avg))
