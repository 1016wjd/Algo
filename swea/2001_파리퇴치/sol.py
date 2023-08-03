import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 전체 보드의 길이
    # M : 파리채의 길이
    N, M = list(map(int, input().split()))

    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    # pprint(matrix)

    # 파리채를 그리기 위한 기준점을 잡기위한 반복문
    total = 0
    for i in range(N-M+1):
        for  j in range(N-M+1):
            # 파리채를 그리는 시작점
            # print(matrix[i][j])

            temp_total = 0

            for row in range(M):
                for col in range(M):
                    temp_total += matrix[i+row][j+col] 
            if total < temp_total:
                total = temp_total

    print(f'#{tc} {total}')





