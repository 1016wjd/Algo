
result = []


for i in range(1,201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)

result = list(map(str, result))  

print(','.join(result))