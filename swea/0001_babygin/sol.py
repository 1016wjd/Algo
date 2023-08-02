import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    #counter = [0 for _ in range(10)] # i가 사용되지 않으면 i 대신 _ 사용/ 0이 10개 채워져있는 리스트 만듬
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]

    for number in numbers:
        counter[int(number)] += 1


   # print(counter)

    idx = 0
    is_babygin = 0
    while idx < len(counter):
        # 1. triplet인지 검증
        if counter[idx] >= 3:
            counter[idx] -=3
            is_babygin += 1 

        # 2. run 인지 검증
        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
        idx +=1

    if is_babygin == 2:
        print(f'#{tc} True')
    else:
        print(f'#{tc} False')




    
