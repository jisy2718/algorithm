# 피보나치 수열을 재귀로 구현했을 때, fibo(0), fibo(1) 이 몇번 호출되는지

T = int(input())
for _ in range(T):
    N = int(input())

    arr = [[0]*(N+1) for _ in range(2)]  # 0행 : 0 호출횟수 / # 1행 : 1 호출횟수
    if N > 1:
        arr[0][0] = 1
        arr[1][1] = 1

        for i in range(2,N+1):
            arr[0][i] = arr[0][i-2] + arr[0][i-1]
            arr[1][i] = arr[1][i-2] + arr[1][i-1]


        print(arr[0][N], arr[1][N])

    elif N == 1:
        print(0, 1)

    elif N == 0:
        print(1, 0)

