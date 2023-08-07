# 인접행렬 방식으로 그래프를 표현
import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # V : 노드수 /E : 간선수
    V, E = list(map(int, input().split()))

    nodes = [ [0] * (V+1) for _ in range(V + 1) ]
    # pprint(nodes)
    
    
    # 인접행렬 방식으로 그래프를 저장
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1
    pprint(nodes)


    # S: 출발노드 / G : 도착노드
    S, G = list(map(int, input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (V+1)


    # dfs 를 구현하기 위한 stack
    stack = []

    now = S
    check_list[now] = True 
    stack.append(now)
    
    result = 0

    # 스택이 비어있지 않으면 계속 반복
    while len(stack):

        now = stack.pop()
        check_list[now] = True

        for link in range(V+1):
            
            # now를 기준으로 연결되어있다면
            if nodes[now][link] == 1:
                # 방문하지 않았다면 
                if not check_list[link] :
                    # 목적지가 연결되어 있다면 
                    if link == G:
                        result = 1

                    # 스택에 추가
                    stack.append(link)

    # print(f'#{tc} {result}')



