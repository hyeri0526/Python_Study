'''
연습문제 3번
i = 1
while i <=5:
    j=1
    while j <= i:
        print("*", end="")
        j = j+1
    print()
    i = i +1

-------------------------------------------
#트리 모양으로 출력
i = 1
while i <= 5:
    j = 5 - i
    while j > 0:
        print(" ", end="")
        j =  j - 1
        
    j = 1
    while j <= ((i-1)*2 +1): 
        print("*",end="")
        j = j +1
    print() # 줄 바꿈
    i = i + 1
'''
i = 1
while i <= 5:
    j = 5 - i
    while j > 0:
        print(" ", end="")
        j =  j - 1
        
    j = 1
    while j <= i : # 1 부터 i 까지 반복
        print("*",end="")
        j = j + 1
    print() # 줄 바꿈
    i = i + 1    
