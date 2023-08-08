import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx):

    if idx >= N :
        print(result)
        return 

    for i in range(N):
        # print(idx, i, '=', numbers[idx][i])
        result.append(numbers[idx][i])
        search(idx+1) # 0부터 반복/ 재귀함수
        result.pop() # 함수 종료 후 실행

for tc in range(1, T+1):
    N = int(input())
    

    numbers = []

    # 모든 경우의 수를 탐색하는 경우
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)
        # numbers.append(list(map(int, input().split()))) # 데이터 input 
    result = []

    search(0)
    # dfs(numbers)
    # print(result)



    
