import sys
sys.stdin = open('input.txt')
from pprint import pprint #이쁘게 출력

T = int(input())

for tc in range(1, T+1):
    
    N=int(input())

    board = [[0 for _ in range(10)] for _ in range(10)]
    # 위와 같은 코드
    # board = []
    # for i in range(10):
    #     temp = []
    #     for _ in range(10):
    #         temp.append(0)
    #         board.append(temp)

    for i in range(N):
        #[2, 2, 4, 4, 1] => r1, c1, r2, c2. color
        color_data = list(map(int, input().split()))

        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]

        #색칠시작

        for x in range(left_top_x, right_bottom_x + 1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color
        # print(board)


    count = 0

    for x in range(board):
        for y in range(board[0]):
            if board[x][y] == 3:
                count += 1

    




