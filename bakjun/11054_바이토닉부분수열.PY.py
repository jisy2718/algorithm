# 증가하는 부분수열 2개(앞에서부터 증가하는 부분수열, 뒤에서부터 증가하는 부분수열) 구해서, 수열의 각 위치에서 합이 가장 큰 것 찾으면 됨

N = int(input())
arr = list(map(int,input().split()))

inc = [[0]*N for _ in range(2)]  # 첫행 : 수열길이, 둘째행 : 최대값
rev_inc = [[0]*N for _ in range(2)]  # 첫행 : 수열길이, 둘째행 : 최대값
inc[0][0]= 1
rev_inc[0][N-1] = 1
inc[1][0] = arr[0]
rev_inc[1][N-1] = arr[N-1]

# 1. 앞에서부터 증가부분수열 찾기
# 자신보다 작은 값 찾을 때까지 앞쪽으로 가기
# 자신보다 작은 값 없다면, 길이 1, 자신이 최대값 부분수열 시작
for i in range(1,N):
    cur = arr[i]

    max_length = 0
    for j in range(i):
        if inc[1][j] < cur and max_length < inc[0][j]:
            max_length = inc[0][j]


    inc[0][i] = max_length + 1
    inc[1][i] = cur


# 2. 뒤에서부터 증가부분수열 찾기
    # 자신보다 작은 값 찾을 때까지 뒤쪽으로 가기 / 자신보다 작은 값 중 길이 max인 것 찾아야함
    # 자신보다 작은 값 없다면, 길이 1, 자신이 최대값 부분수열 시작
for i in range(N-2, -1,-1):
    cur = arr[i]

    max_length = 0
    for j in range(i+1,N):
        if rev_inc[1][j] < cur and max_length < rev_inc[0][j]:
            max_length = rev_inc[0][j]

    rev_inc[0][i] = max_length + 1
    rev_inc[1][i] = cur




sum_dp = [0]*N
for i in range(N):
    sum_dp[i] = inc[0][i] + rev_inc[0][i]

for row in inc:
    print(row)
print()

for row in rev_inc:
    print(row)
print()

print(max(sum_dp)-1)




