import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : 화덕 크기 / M : 피자 개수
    N, M = list(map(int, input().split()))
    ci = list(map(int, input().split()))
    
    before = [] # 구워지기 전 피자
    for i in range(M):
        before.append([ci[i],i])
        
    # print(before)
    
    # 화덕 
    queue = [0] * N

    # 완성피자를 저장할 목록 
    after = []
    

    # 완성피자가 구워야하는 피자 갯수랑 같아질때까지 반복
    while len(after) != M:

        # 화덕 입구에 공간이 비었으면  
        if queue[0] == 0:
            # 넣을 파지가 있으면
            if len(before) != 0:
                # 남은 첫번째 치즈와 번호
                cheeze, idx = before.pop(0) # 맨처음이 나가고
                # 화덕에 넣기 
                queue.append([cheeze, idx]) # 맨뒤에 들어감
            #넣을 피자가 없을 때 
            else:
                queue.pop(0)
                queue.append(0) 
        # 화덕 입구에 공간이 없으면 (이미 구워지고 있는 피자가 있는 경우)
        else:   
            # 치즈 절반 감소
            queue[0][0] //= 2

            # 치즈가 다 녹았는지 확인
            if queue[0][0] == 0:
                # 완성된 피자 꺼내기
                pizza = queue.pop(0)
                # 완성 목록에 넣기
                after.append(pizza)

                if len(before) != 0:
                    # 남은 첫번째 치즈와 번호
                    cheeze, idx = before.pop(0)
                    # 화덕에 넣기
                    queue.append([cheeze, idx])
                else:
                    queue.append(0)
            else:
                queue.append(queue.pop(0))

    print(after[-1][-1]+1)

                
        












#     turn_count = []
#     for i in range(M):
#         turn_count.append(Ci[i]//2)

#     # print(turn_count)

    
#     MAX = 0
#     idx = []
#     for i in range(M):
#         if MAX < turn_count[i]:
#             MAX = turn_count[i]
            
#     print(list(filter(lambda x: turn_count[x] == MAX, range(len(turn_count)))))
# #    print(turn_count.index(MAX))
# #    print(MAX)