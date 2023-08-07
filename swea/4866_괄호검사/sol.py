import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    code = input()
    stack = []

    for char in code:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)
        if len(stack) == 0:
            result = 1
        else:
            result = 0

    print(f'#{tc} {result}')

        #print(char) # 한글자씩 출력

    #현정 코드 미완성
    # message = input()
    # # print(message)
    
    # a = message.count('(')
    # b = message.count(')')
    # c = message.count('{')
    # d = message.count('}')

    
    # if a == b:
    #     pass
    # else:
    #     result = 0
    #     break
    #     if c == d:
    #         pass
    #     else:
    #         result = 0
    #         break
    #        



    # print(result)       
            
     
        