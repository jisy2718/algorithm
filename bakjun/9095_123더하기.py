
def dfs(n):
    global result

    if n == 0 :
        result += 1
        return
    else:
        if n - 1 >= 0:
            dfs(n-1)
        if n - 2 >= 0:
            dfs(n-2)
        if n - 3 >= 0:
            dfs(n-3)




T = int(input())
for _ in range(T):
    N = int(input())
    result = 0
    dfs(N)
    print(result)

