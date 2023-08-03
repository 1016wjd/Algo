import sys
sys.stdin = open('input.txt')

# N = int(input())

# if N % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')


TC = int(input()) #9는 횟수로 들어감

for i in range(TC):
    N = int(input())
    
    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')



# 1차원 리스트
# numbers = input().split()
# #print(numbers)
# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다')



numbers = list(map(int,input().split()))
#input으로 받아온 문자를 숫자리스트 형태로 변환
for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다')
    

# 2차원 리스트 input 받기
N = int(input())
matrix = []

for i in range(3):
    numbers = list(map(int,input().split())) #숫자리스트 형태로 변경
    matrix.append(numbers) #매트릭스로 변경

print(matrix)

for row in matrix:
    print(row)
    for item in row:
        if item == 5: # 10 넣으면 결과물 없음
            print('5가 있습니다')

# 4*5 list로 만들기
N, M = map(int,input().split())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)
print(matrix)



#아래의 코드와 같은의미
# for row in range(len(matrix)): #매트릭스의 길이(=세로의 길이 = 행의 개수)만큼 반복
#     for col in range(len(matrix[0])): #매트릭스의 0번 데이터의 길이 (=가로의 길이 = 열의 개수)

# 행먼저
# for row in range(N): 
#     for col in range(M):
#         print(matrix[row][col])

# 열먼저
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col])


