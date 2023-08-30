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


    # print(maze)

    # 시작점찾기

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                maze[i][j] = -1

    # pprint(start)

    #  dfs를 동작하기 위한 스택
    queue = []
    queue.append(start)
    # queue = [start]

    distance = [([0] * N ) for _ in range(N)]

    # 거리를 계산하기 위한 코드
    # pprint(distance)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = 0
   
    
    while len(queue):

        now = queue.pop(0)
        x, y = now[0], now[1]


        # 상하좌우를 바라보는 코드
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 안에 있다면 진행 
            if 0 <= nx < N and 0 <= ny < N:
        
                
                # print(nx, ny)

                # 길이라면 
                if maze[nx][ny] == 0:
                    queue.append( (nx, ny) )
                    maze[nx][ny] = maze[x][y] -1
                    

                # 도착지점이라면 
                elif maze[nx][ny] == 3:
                    result = abs(maze[x][y]) -1
                    

                    
                    break

    print(result)