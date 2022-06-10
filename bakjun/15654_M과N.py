

N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

perm = [0]*M
def dfs(idx,used):
    if idx == M:
        print(*perm)
        return

    # 앞자리부터 숫자를 택하는데, 가장 작은 숫자부터 loop 돌면서, 이전에 안 쓴거면 사용하기!
    # 그렇게 하면, 사전순으로 모든 조합 가능!
    for i in range(N):
        if arr[i] not in used:
            perm[idx] = arr[i]
            used.add(arr[i])
            dfs(idx+1, used)
            used.remove(arr[i])

used= set()
dfs(0, used)