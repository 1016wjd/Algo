a = 3 
b = 5
def solution(a, b):
    if a%2 ==0 and b%2==0:
        answer = abs(a-b)
    elif a%2 == 1 and b%2== 1:
        answer = a**2 + b**2
    else:
        answer = 2*(a + b)
    return answer


print(solution(a, b))