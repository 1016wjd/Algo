#sol1
def solution(numbers):
    answer = 0
    
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    
    return answer

#sol2
# def solution(numbers):
#     answer = 0
#     n = numbers.sort(reverse=True)
#     n1 = numbers[0]
#     n2 = numbers[1]
#     answer = n1 * n2
#     return answer

def solution(numbers):
    answer = 0
    
    #인덱스찾기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            #print(i,j)
            result = numbers[i] * numbers[j]
            
    if answer < result:
        answer = result
        
    return answer