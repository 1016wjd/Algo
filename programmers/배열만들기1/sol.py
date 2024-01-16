n = 10
k = 3



    
    
def solution(n, k):
    m = n // k
    answer = []
    for i in range(1,m+1):
        answer.append(i*k)
    return answer

print(solution(n, k))