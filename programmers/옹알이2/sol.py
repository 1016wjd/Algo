# babbling = ["aya", "yee", "u", "maa", "wyeoo"]
# babbling = ["aya", "yee", "u", "maa"]
# babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
# result = 0
# for i in range(len(babbling)):
#     for j in ["aya", "ye", "woo", "ma"]:
#         if j in babbling[i]:
#             # print(babbling[i].replace(j,"."))
#             babbling[i] = babbling[i].replace(j,".",1)
             
# for word in babbling:
#     if all(char == '.' for char in word):
#         result += 1 

# print(result)
# print(babbling)


def solution(babbling):
    result = 0
    for i in range(len(babbling)):
        for j in ["aya", "ye", "woo", "ma"]:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j,".",1)
                
    for word in babbling:
        if all(char == '.' for char in word):
            result += 1 
    return print(result)


babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
solution(babbling)

## 테스트 2개는 맞는데 제출 틀림 ㅠㅡㅠ