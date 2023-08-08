import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited, SUM):
    global MIN_SUM

    if idx >= N :
        # print(result, sum(result)
        # print(SUM)
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        return 

    if SUM > MIN_SUM:
        return

    for i in range(N): # i 는 열 의미
        if visited[i] == False: # 세로줄 제외하기 
            # print(idx, i, '=', numbers[idx][i])
            # result.append(numbers[idx][i])
            SUM += numbers[idx][i]
            visited[i] = True 
            search(idx+1, visited, SUM) # 0부터 반복/ 재귀함수
            
            # result.pop() # 함수 종료 후 실행
            SUM -= numbers[idx][i]
            visited[i] = False
for tc in range(1, T+1):
    N = int(input())
    

    numbers = []

    # 모든 경우의 수를 탐색하는 경우
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)
        # numbers.append(list(map(int, input().split()))) # 데이터 input 
    result = []
    visited = [False] * N

    SUM = 0
    MIN_SUM = 100000000

    search(0, visited, SUM)
    print(f'{tc} {MIN_SUM}')

    
    # dfs(numbers)
    # print(result)

  

    




    
