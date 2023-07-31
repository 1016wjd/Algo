# def solution(n):
#     answer = 0

#     while a > 0:
#         a, b = divmod(n, 10)

#         n = a
#         answer += b 

#         return answer

def solution(n):
    answer = 0
    for i in str(n):
        answer = answer + int(i)
        # answer += int(i)
        # answer = list(map(len,strlist))
    return answer