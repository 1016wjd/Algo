money = 15000

# print(money // 5500)
# print(money % 5500)

def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    
    return answer

print(solution(money))