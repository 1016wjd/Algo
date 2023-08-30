import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def inorder(idx):
    global count
    if idx <= N:

        # 왼쪽자식
        inorder(idx*2)
        
        # 현재 노드
        tree[idx] = count
        count += 1
        
        # 오른쪽자식 
        inorder(idx*2 + 1)

        
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    count = 1
    # 중위순회

    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')