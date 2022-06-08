N = int(input())
arr = list(map(int, input().split()))
# print(arr)
dp = [0] * N

dp[0] = 1

for i in range(1, N):
    cur = arr[i]
    max_idx = -1
    max_length = -1
    # 자기 이전의 dp에서 자신보다 작은 수 중, 최대 수열 개수 구해서 +1 해주면 됨
    for j in range(i):
        # 1.자신 보다 이전에 있는 수열들 중에서, 자신보다 작은 수 찾기
        if arr[j] < cur:
            # 2. 자신보다 작은 수 중에서, 부분수열 길이가 최대인 것 찾기
            if dp[j] > max_length:
                max_length = dp[j]
                max_idx = j

    # 3. 자신보다 작은 수 중에서, 부분수열 길이가 최대인것 +1 하면, 현재까지 최대 부분수열길이
    if max_idx == -1:  # 자신보다 작은 수가 없는 경우
        dp[i] = 1
    else:
        dp[i] = dp[max_idx] + 1
    # print(dp)

print(max(dp))