import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # P : 책의 장수(마지막페이지)
    # A : A가 찾아야 하는 목적페이지 
    # B : B가 찾아야 하는 목적페이지
    P, A, B = list(map(int, input().split()))

    count_a = 0
    left = 1
    right = P


    while True: # 무한한 반복
        middle = int((left + right)/2) # 중앙값
        
        # 목적페이지가 가운데보다 왼쪽에 있는경우
        if A < middle:
            right = middle
        # 목적페이지가 가운데보다 오른쪽에 있는경우
        elif middle < A:
            left = middle
        # 둘다 아니라면 목적페이지에 도착! 
        else:
            break

        count_a += 1

    count_b = 0
    left = 1 
    right = P

    while True: # 무한한 반복
        middle = int((left + right)/2) # 중앙값
        
        # 목적페이지가 가운데보다 왼쪽에 있는경우
        if B < middle:
            right = middle
        # 목적페이지가 가운데보다 오른쪽에 있는경우
        elif middle < B:
            left = middle
        # 둘다 아니라면 목적페이지에 도착! 
        else:
            break

        count_b += 1
    
    # print(count_a, count_b)

    result = ''
    if count_a > count_b:
        print(f'#{tc} B')
    elif count_a < count_b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} O')

