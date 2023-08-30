import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))


    for i in range(M):
        # 직접 M번 반복
        data = numbers.pop(0)
        numbers.append(data)

        # 현정코드
        # numbers.append(numbers[0])
        # numbers.pop(0)

        # remain = N % M 만큼반복가능 

    print(f'#{tc} {numbers[0]}')
    # print(M, N, numbers) # 데이터 입력 학인



