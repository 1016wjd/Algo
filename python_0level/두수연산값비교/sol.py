a = 2
b = 91 

def solution(a, b):
    ans1 = int(str(a) + str(b))
    ans2 = 2 * a * b 
    answer = max(ans1, ans2)
    return answer

print(solution(a, b))