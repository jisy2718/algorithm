# 값이 더 커지려면, 이전 까지의 연속된 값의 합이 양수이고, 현재 값을 이전까지 값에 더했을 때도 양수가 되어야 함.
# 그렇지 않으면, 그냥 새로 시작해야 함


N = int(input())

arr = list(map(int,input().split()))

dp = arr.copy()
max_val = max(dp)
for i in range(1,N):
    # 이전 까지의 합이 양수여야, i번째 값을 갱신함
    if dp[i-1] > 0:
        # 이전 까지의 값과, 현재 i번째 값을 더해서 양수여야, i번재 값을 갱신함
        if dp[i-1] + dp[i] > 0:
            dp[i] = dp[i-1] + dp[i]

    if dp[i] > max_val:
        max_val = dp[i]

print(max_val)
