import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())



# 현정코드
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     strings = [input() for _ in range(N)]
#     string_col = list(zip(*strings)) #행열변환
     
#     result = ''
#     for i in range(N):
#         #row비교
#         for j in range(N-M+1):
#             if strings[i][j:j+M] == strings[i][j:j+M][::-1]:
#                 result = strings[i][j:j+M]
#         #col비교
#         for k in range(N-M+1):
#             if string_col[i][k:k+M] == string_col[i][k:k+M][::-1]:
#                 result = ''.join(string_col[i][k:k+M])
          
#     print(f'#{tc} {result}')

# 선생님 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())

    string_map = []
    for string in range(N):
        string_map.append(input()) # => 'GOFFAKWSM' 2 차원 리스트와 같다!
        # string_map.append(list(input())) # => ['G', 'O',...]
    # pprint(string_map)

    result = []

    # 가로 기준점/ 회문의 시작점을 찾기 위한 코드
    for row in range(N):
        for col in range(N-M+1):
            # print(string_map[row][col]) 
           
            for i in range(M//2):
                # front : 앞글자
                f = string_map[row][col+i]
                # back : 뒷글자
                b = string_map[row][col+M-1-i]
                
                # 앞뒤가 똑같다면 
                if f == b:
                    continue 
                # 똑같지 않다면
                else:
                    break
            #for을 끝까지 도는 경우/ break를 만나지 않은 경우 = > 회문을 찾았다!
            else: 
                for a in range(M):
                    result.append(string_map[row][col+a])

                
    #세로 기준점/ 회문의 시작점을 찾기위한 코드 
    for col in range(N):
        for row in range(N-M+1):
            for i in range(M//2):
                # front : 앞글자
                f = string_map[row+i][col]
                # back : 뒷글자
                b = string_map[row+M-1-i][col]
                
                # 앞뒤가 똑같다면 
                if f == b:
                    continue 
                # 똑같지 않다면
                else:
                    break
            #for을 끝까지 도는 경우/ break를 만나지 않은 경우 = > 회문을 찾았다!
            else: 
                for a in range(M):
                    result.append(string_map[row+a][col])

    print(''.join(result))


            
# 서연님 코드
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     board = []

#     for _ in range(N): #N + 1 > N 
#         r = list(input().split())
#         board.append(r[0])

#         for row in range(N):
#             for i in range(N-M+1):
#                 for word in range(M // 2):
              
#                     if board[i][j:j+word] == board[i][::-1]:
#                     else:
#                         pass

#         for col in range(N):
#             count_c = 0
#             for j in range(N-M+1):
#                 for word in range(M // 2):
#                     if board[word] != board[-1 -word]:
#                         count_c += 1
#                     else:
#                         pass

#     print(f'#{tc} {count_c + count_r}')

        
        
    

        
                         
                        








