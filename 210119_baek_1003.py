# https://www.acmicpc.net/problem/1003

t = int(input())

def fibo(n):
    cach = [[0, 0] for i in range(n+1)]
    cach[0] = [1, 0]
    if len(cach) > 1:
        cach[1] = [0, 1]
        for i in range(2, len(cach)):
            cach[i][0] = cach[i-1][0] + cach[i-2][0]
            cach[i][1] = cach[i-1][1] + cach[i-2][1]
    return cach[-1]

for _ in range(t):
    print(*fibo(int(input())))

# 다른사람 풀이

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     if n == 0:
#         print(1, 0)
#         continue
#     a = 0
#     b = 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     print(a, b)