import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # E : 간선의 개수 N : 루트로 하는 서브트리
    E, N = map(int,input().split())

    nodes = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)
    
    for  i in range(0, E * 2, 2):
        parent = nodes[i]
        child = nodes[i+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    # print(left)
    # print(right)
    


    count = 0
    stack = [N]

    while stack:
        now = stack.pop() 
        count += 1 
        
        if left[now]: # 자식1이 있다면
            stack.append(left[now])

        if right[now]:
            stack.append(right[now])

    print(count)
 
    
