coffee = 10

while True:   # 무한 반복
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 수는 %d 개 입니다. " % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        break   # 반복을 중단
print("휴식을 길어지면 몸이 아파집니다.")
