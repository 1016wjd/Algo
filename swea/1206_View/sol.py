import sys
sys.stdin = open('input.txt')


#데이터 입력
for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))
    # print(N,H)

    # 내코드
    count = 0
    
    for i in range(2, N-2):
        gap1 = H[i] - H[i-2]
        gap2 = H[i] - H[i-1]
        gap3 = H[i] - H[i+1]
        gap4 = H[i] - H[i+2]
        if gap1>0 and gap2>0 and gap3>0 and gap4>0:
            count += min(gap1, gap2, gap3, gap4)
        else:
            pass
        
    # print(count)

    print(f'#{tc} {count}')



    # #선생님 코드
    # total = 0
    # for i in range(N):
    #     now = H[i]
    #     # 현재 위치에 건물이 없다면 다른 건물로 넘어감
    #     if now == 0:
    #         continue
        
    #     # 나의 위치에 건물이 있는 경우
    #     else:
    #         #양옆 * 2 건물의 높이 비교

    #         dx = [-2, -1, 1, 2]

    #         max_tall = 0

    #         for j in range(4):
    #         # i : 현재위치 
    #         # dx[j] : 기준건물을 중심으로 좌우 인덱스
    #             comp = H[i+dx[j]]

    #             if max_tall < comp:
    #                 max_tall = comp

    #         if now > max_tall:
    #             view = now - max_tall
    #             total +=   view

    # print(f'#{tc} {total}')
        
