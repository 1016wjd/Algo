numbers = list(range(1,13))

# 부분집합을 구하는 배열의 길이 

n = len(numbers)

# 모든 부분집합의 경우의 수 만큼 반복문을 실행
for i in range(1<<n): # 10000 = 2의 5승 = 32 2진수로 변환?
    # print(i, bin(i)) # bin 이진수표현

    temp = []
    for j in range(n):
        print(bin(i), bin(1<<j))
        if i & (1<<j):
            temp.append(numbers[j])


    # print(temp)numbers = list(range(1,13))

n = len(numbers)

for i in range(1<<n):
    # print(i, bin(i))

    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(numbers[j])

    print(temp)