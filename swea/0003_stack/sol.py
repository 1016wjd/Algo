memo = [0, 1]

def fibo(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1)+ fibo(n-2))
    return memo[n]


print(fibo(100))


# 재귀함수이지만 연산된 데이터를 저장하고 출력하므로 더 빠름