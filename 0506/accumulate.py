'''
hap = 0
i = 1
while i <= 100:
    hap = hap + i
    i = i+1

print("합 = %d" %hap)
------------------------------------------------------------------
evenHap = 0
oddHap = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        evenHap = evenHap + i
    else:
        oddHap = oddHap + i
    i = i + 1

print("짝수의 합 = %d" %evenHap)
print("홀수의 합 = %d" %oddHap)
------------------------------------------------------------------

sevenHap = 0
i = 1
while i <= 100:
    if i % 7 == 0:
        sevenHap = sevenHap + i
    i = i + 1

print("1-100 7의 배수 합 = %d" %sevenHap)
------------------------------------------------------------------

hap = 0
i = 1
while i <= 100:
    hap = hap + i
    if hap >= 1000 :
        break
    i = i + 1

print("1-100 중 처음으로 1000을 넘는 수는  %d이고, 합 = %d" %(i, hap))
'''
hap = 0
i = 0
while i <= 100:
    i = i + 1
    if i % 7 == 0 :
       continue   # 7의 배수이면 아래 명령어 실행하지 않고 while 반복문 실행.
    hap = hap + i
print("1-100 합 중에 7의 배수를 생략한 합 = %d" %hap)


