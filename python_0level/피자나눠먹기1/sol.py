n = 7


def solution(n):
    pan = n // 7 
    if n % 7 == 0:
        answer = pan
    else:
        answer = pan + 1
    return answer

print(solution(n))