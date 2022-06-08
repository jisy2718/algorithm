N = int(input())
answer = list(input())

solutions = [ list(input()) for _ in range(N)]

M = len(answer)

# 1. [1,2,3]의 부분집합 생성
arr = list(range(N))

results = []        # 결과들 다 list로 저장
for i in range(1<<N):
    subset = []
    for j in range(N):
        # j번째 자리가 1인지 파악
        if i & (1<<j):
            subset.append(arr[j])
    results.append(subset)

INF = 0xfffffffffff
min_result = INF
# print(results)
for result in results:
    sol = [0]*M
    # i번 문제
    for i in range(M):
        ans = answer[i]
        flag = False
        # 모든 사람들이 i번 문제 풀었는지 탐색
        for person in result:
            cur_sol = solutions[person]

            if cur_sol[i] == ans:
                sol[i] = 1

    if sum(sol) == M:
        cur_val = len(result)
        if min_result > cur_val:
            min_result = cur_val

if min_result == INF:
    print(-1)
else:
    print(min_result)





