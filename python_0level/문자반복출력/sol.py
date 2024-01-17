my_string = "hello"
n = 3 

def solution(my_string, n):
    answer = ""
    for i in my_string:
       answer +=  i*n
    return answer

print(solution(my_string, n))