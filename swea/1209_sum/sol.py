import sys
sys.stdin = open('input.txt')

# 2차원 데이터 리스트로 입력
T = 10
for tc in range(1, T + 1):
    tc = int(input())

    matrix = []

    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)

    
    total = 0
    # 가로줄 반복 
    #range(100) 가능
    for row in range(len(matrix)):
        temp = 0
        for col in range(len(matrix[0])):
            temp += matrix[row][col]
        if total < temp:
            total = temp

    # 세로줄 반복 
    for col in range(100):
        temp = 0
        for row in range(100):
            temp += matrix[row][col]
        if total < temp:
            total = temp
    

    # 좌상단 => 우하단 반복
    temp = 0
    for i in range(100):
        temp += matrix[i][i]
    if total < temp:
        total = temp

    # 우상단 => 좌하단
    temp = 0
    for i in range(100):
        temp += matrix[i][99-i]
    if total < temp:
        total = temp


    print(f'#{tc} {total}')   
        
        


        


        




