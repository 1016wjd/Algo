import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


T = int(input())

memo = [0, 1, 3]


for tc in range(1, T+1):
    N = int(input()) // 10

    #memo 배열에 출력시킬 값이 없으면 추가
    while N >= len(memo):
        # n-2 배열에 가로로 작은 사각형 두개 쌓거나 혹은 큰 사각형 쌓는 방법 (X2)
        # n-1 배열에 세로로 작은 사각형 쌓느 방법 하나
        temp = memo[len(memo)-2] + memo[len(memo) - 1]
        
        memo.append(temp)
    print(temp)
    print(f'#{tc} {memo[N]}')



# # 블로그 풀이
# m = [1, 1]                          # f(0) = 1, f(1) = 1
# for i in range(2, 31):              # 문제의 조건에서 f(30)까지 필요
#     m.append(m[i-1] + 2*m[i-2])     # 점화식 f(n) = f(n-1) + 2*f(n-2)
 
# for tc in range (1, T+1):
#     N = int(input())//10            # 10의 배수를 종이의 폭으로 나눔
#     print('#{} {}'.format(tc, m[N]))
            
    



    

