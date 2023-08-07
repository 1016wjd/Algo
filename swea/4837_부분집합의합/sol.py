import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    numbers = list(range(1,13))
    N, K = list(map(int, input().split()))
    count = 0
    
    #부분집합 만들기
    for i in range(1 << len(numbers)):
        temp = [] 
        for j in range(len(numbers)):
            if i & (1<< j): # 각 자리수를 비교해서 0이면 F 숫자면 T로 반환
                temp.append(numbers[j]) # 각 자리수가 존재하면 true를 반환함

        #부분집합 비교하기
        if len(temp) == N and sum(temp) == K:
            count += 1

    print(f'#{tc} {count}')
