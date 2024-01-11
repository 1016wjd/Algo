# babbling = ["aya", "yee", "u", "maa", "wyeoo"]
babbling = ["yeye","ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
result = 0
for i in range(len(babbling)):
    for j in ["aya", "ye", "woo", "ma"]:
        if j in babbling[i]:
            # print(babbling[i].replace(j,"."))
            babbling[i] = babbling[i].replace(j,".")
             
for word in babbling:
    if all(char == '.' for char in word):
        result += 1 

print(result)
# print(babbling)


            
def solution(babbling):
    result = 0
    for i in range(len(babbling)):
        for j in ["aya", "ye", "woo", "ma"]:
            if j in babbling[i]:
                # print(babbling[i].replace(j,"."))
                babbling[i] = babbling[i].replace(j,".")
                
    for word in babbling:
        if all(char == '.' for char in word):
            result += 1 

    print(result)




