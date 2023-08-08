# 인접리스트 방식으로 그래프 표현 => 재귀함수를 이용하여 풀이
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def dfs(now):
    #방문체크
    check_list[now] = True

    # print(check_list) # 함수의 방문 체크
    # 현재 위치를 기준으로 연결된 
    for link in nodes[now]:
        # 방문하지 않은 노드들은 스택에 추가
        if not check_list[link]:
            dfs(link)

     

for tc in range(1, T+1):
    # V : 노드수 /E : 간선수
    V, E = list(map(int, input().split()))

    nodes = [ []  for _ in range(V + 1) ]
    # pprint(nodes)
    
    
    # 인접리스트 방식으로 그래프를 저장
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start].append(end) 
    # pprint(nodes)

    
    # S: 출발노드 / G : 도착노드
    S, G = list(map(int, input().split()))



    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    dfs(S)

    if check_list[G]:
        result = 1
    else:
        result = 0

    print(result)

    
