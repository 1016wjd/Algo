str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"

answer = 2
n = len(str1) - len(str2) + 1
for i in range(n):
    if str2 == str1[i:i+len(str2)]:
        answer = 1
        
print(answer)