num_list = [1, 3, 5, 7]

num_0 = 0
num_1 = 0

for i in num_list:
    if i % 2 == 0:
        num_0 += 1 
    else:
        num_1 += 1
answer = []
answer.append(num_0)
answer.append(num_1)
print(answer)
        