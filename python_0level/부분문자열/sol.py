str1 = "abc"
str2 = "aabcc"


result = 0
n = len(str2) - len(str1) + 1
# print(len(str2) - len(str1) + 1) 
for i in range(n):
    if str1 == str2[i:i+len(str1)]:
        result = 1 
    # print(str2[i:i+len(str1)])
    
print(result)