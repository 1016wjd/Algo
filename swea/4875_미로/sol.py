import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    maze = [list(map(int, list(input()))) for _ in range(N)]


    # pprint(maze)

    # 시작점찾기

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
    # print(start)

    # for i in range(n):
    #     if 2 in map_list[i]
    #         x = map_list[i].index(2)
    #         y = i
    #         break


    #  dfs를 동작하기 위한 스택
    stack = []
    stack.append(start)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0 
    
    while len(stack):

        now = stack.pop()
        x, y = now[0], now[1]

        maze[x][y] = 1 # 방문기록

        # 상하좌우를 바라보는 코드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:
                # print(nx, ny)

                # 길이라면 
                if maze[nx][ny] == 0:
                    stack.append( (nx, ny) )
                # 도착지점이라면 
                elif maze[nx][ny] == 3:
                    result = 1
                    break

    pprint(result)

        

    