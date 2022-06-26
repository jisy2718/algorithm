N, M = map(int,input().split())
arr = list(map(int,input().split()))

p=[0]*M
def dfs(idx,start):
    if idx ==M:
        print(*p)
        return

    for i in range(start,N):
        p[idx] = arr[i]
        dfs(idx+1,i)



arr.sort()

dfs(0,0)
