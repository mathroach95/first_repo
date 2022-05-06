# 과제 1부터 20까지 반복하는 과정에서 3의 배수일 경우 year를 출력하시오.
# 추가과제 : 5의 배수일 때, deam 출력
# 나머지 모든 경우는 숫자 그대로 출력
for i in range(1,21):
    if i % 3 == 0:
        if i % 5 == 0:
            print('year dream')
        else:
            print('year')
    elif i % 5 == 0:
        print('dream')
    else:
        print(i)
