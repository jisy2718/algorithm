
T = int(input())
for _ in range(T):



    # nCr = n-1Cr-1 + n-1Cr
    nCr = [[0]*30 for _ in range(30)] # 1 행 : n, 2행 : r

    nCr[2][1] = 2

    for n in range(30):
        nCr[n][0] = 1
        nCr[n][n] = 1


    R, N = map(int,input().split())

    def perm(N,R):
        # 계산이 안된 경우
        if nCr[N][R] == 0:
            temp = perm(N-1,R-1) + perm(N-1,R)
            nCr[N][R] = temp
            return temp
        # 계산이 이미 된 경우
        else:
            return nCr[N][R]

    print(perm(N,R))



