import sys
input = sys.stdin.readline

N = int(input())



max_dp = [[0]*3 for _ in range(2)]
min_dp = [[0]*3 for _ in range(2)]




for i in range(0,N):
    # 처음 경우
    if i == 0 :
        arr = list(map(int,input().split()))
        max_dp[0] = arr.copy()
        min_dp[0] = arr.copy()
    else:
        new = list(map(int,input().split()))
        # i 번째 줄
        # 1. 처음은, 이전 줄의 처음과 중간 값에서 이동가능
        max_dp[1][0] = new[0] + max(max_dp[0][0:2])
        min_dp[1][0] = new[0] + min(min_dp[0][0:2])

        # 2. 두번째는, 이전 줄의 모든 곳에서 이동 가능
        max_dp[1][1] = new[1] + max(max_dp[0][0:3])
        min_dp[1][1] = new[1] + min(min_dp[0][0:3])
        # 3. 마지막은, 이전 줄의 중간과 마지막에서 이동가능
        max_dp[1][2] = new[2] + max(max_dp[0][1:3])
        min_dp[1][2] = new[2] + min(min_dp[0][1:3])

        max_dp[0] = max_dp[1].copy()
        min_dp[0] = min_dp[1].copy()





print(max(max_dp[0]), min(min_dp[0]))